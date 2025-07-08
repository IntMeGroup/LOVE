import gc
import json
import logging
import math
import os
import random
import sys
import traceback
import warnings
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, Optional

import numpy as np
import torch
import torch.distributed as dist
import transformers
from dist_utils import init_dist
from model.internlm2.modeling_internlm2 import InternLM2ForCausalLM
from model.internvl_chat_infer import (InternVisionConfig,
                                          InternVisionModel,
                                          InternVLChatConfig,
                                          InternVLChatModel)
from patch import (concat_pad_data_collator,
                            replace_llama_rmsnorm_with_fused_rmsnorm,
                            replace_train_sampler)
from train.constants import (BOX_END_TOKEN, BOX_START_TOKEN,
                                      IMG_CONTEXT_TOKEN, IMG_END_TOKEN,
                                      IMG_START_TOKEN, QUAD_END_TOKEN,
                                      QUAD_START_TOKEN, REF_END_TOKEN,
                                      REF_START_TOKEN)
from train.dataset import (ConcatDataset, TCSLoader,
                                    WeightedConcatDataset, build_transform,
                                    dynamic_preprocess, preprocess,
                                    preprocess_internlm, preprocess_mpt,
                                    preprocess_phi3)
from train.trainer_monkey_patch import replace_create_optimizer
from PIL import Image, ImageFile, PngImagePlugin, UnidentifiedImageError
from torch.utils.data import Dataset
from transformers import (AutoConfig, AutoModelForCausalLM, AutoTokenizer,
                          HfArgumentParser, Trainer, TrainingArguments,
                          set_seed)
from transformers.trainer_utils import get_last_checkpoint
from transformers.utils.logging import (enable_default_handler,
                                        enable_explicit_format, set_verbosity)
import pandas as pd
from scipy.stats import spearmanr, pearsonr, kendalltau
import torch.optim as optim
from tqdm import tqdm

# Apply necessary patches for the transformers library
replace_llama_rmsnorm_with_fused_rmsnorm()
replace_train_sampler()

# Try to import petrel_client for image loading, fallback to PIL if unavailable
try:
    from petrel_client.client import Client
    from petrel_client.common.config import Config
    has_tcs_loader = True
except ImportError as E:
    print('petrel_client is not installed. Using PIL to load images.')
    has_tcs_loader = False

# Set constants for image processing and logging
IGNORE_INDEX = -100
IGNORE_INDEX2 = 92542
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True
MaximumDecompressedSize = 1024
MegaByte = 2 ** 20
PngImagePlugin.MAX_TEXT_CHUNK = MaximumDecompressedSize * MegaByte

warnings.filterwarnings('ignore')
logger = logging.getLogger(__name__)

os.environ['TOKENIZERS_PARALLELISM'] = 'true'
@dataclass
class CustomArguments:
    """
    Custom arguments for additional configurations like output files.
    """
    output_file: Optional[str] = field(
        default='results.csv',
        metadata={'help': 'The name of the CSV file to save evaluation results.'}
    )
    metrics_file: Optional[str] = field(
        default='metrics.txt',
        metadata={'help': 'The name of the TXT file to save evaluation metrics.'}
    )
    
@dataclass
class ModelArguments:
    """
    Arguments for specifying model, tokenizer, and configurations.
    """
    model_name_or_path: Optional[str] = field(
        default=None,
        metadata={'help': 'Path to pretrained model or model identifier from huggingface.co/models'}
    )
    vision_path: Optional[str] = field(
        default=None,
        metadata={'help': 'Path to pretrained model or model identifier from huggingface.co/models'}
    )
    llm_path: Optional[str] = field(
        default=None,
        metadata={'help': 'Path to pretrained model or model identifier from huggingface.co/models'}
    )
    mlp_path: Optional[str] = field(
        default=None,
        metadata={'help': 'Path to pretrained model or model identifier from huggingface.co/models'}
    )
    freeze_llm: bool = field(
        default=False,
        metadata={'help': 'Set to True to freeze the LLM decoder.'},
    )
    freeze_backbone: bool = field(
        default=False,
        metadata={'help': 'Set to True to freeze the vision backbone of the model.'},
    )
    freeze_mlp: bool = field(
        default=False,
        metadata={'help': 'Set to True to freeze the MLP layers of the model.'},
    )
    unfreeze_vit_layers: int = field(
        default=0,
        metadata={'help': 'Specify the number of ViT layers to unfreeze. Default is 0.'},
    )
    vision_select_layer: int = field(
        default=-1,
        metadata={'help': 'Specify the layer of ViT feature map to use. Default is last layer.'},
    )
    use_backbone_lora: int = field(
        default=0,
        metadata={'help': 'Set the LoRA adapter rank for the backbone model. Default is 0.'}
    )
    use_llm_lora: int = field(
        default=0,
        metadata={'help': 'Set the LoRA adapter rank for the LLM. Default is 0.'}
    )
    unfreeze_lm_head: bool = field(
        default=False,
        metadata={'help': "Set to True to unfreeze the language model's head."},
    )
    use_custom_trainer: bool = field(
        default=False,
        metadata={'help': 'Set to True to enable the use of a custom trainer.'},
    )
    grad_checkpoint: Optional[bool] = field(
        default=False,
        metadata={'help': 'Set to True to use gradient checkpointing.'},
    )
    drop_path_rate: float = field(
        default=0.0,
        metadata={'help': 'Set the drop path rate for the ViT model. Default is 0.'},
    )
    ps_version: str = field(
        default='v2',
        metadata={'help': 'Specify the version of pixel shuffle implementation. Default is `v1`.'
                          'Please use `v2` to fix the bug of transposed image.'}
    )


@dataclass
class DataTrainingArguments:
    """
    Arguments for specifying data input for training and evaluation.
    """
    max_seq_length: Optional[int] = field(
        default=2048,
        metadata={
            'help': (
                'The maximum total input sequence length after tokenization. Sequences longer '
                'than this will be truncated, sequences shorter will be padded.'
            )
        },
    )
    force_image_size: Optional[int] = field(
        default=448,
        metadata={'help': 'Set the desired size for the image. Default is 224.'},
    )
    down_sample_ratio: Optional[float] = field(
        default=0.5,
        metadata={'help': 'Set the desired down-sampling ratio for the image. Default is 1.0.'},
    )
    pad2square: Optional[bool] = field(
        default=False,
        metadata={'help': 'Pad the image to a square shape if set to True.'},
    )
    conv_style: Optional[str] = field(
        default='internlm2-chat', metadata={'help': 'Prompt style for a conversation.'}
    )
    meta_path: Optional[str] = field(
        default=None,
        metadata={'help': 'The path of the meta file of datasets.'},
    )
    use_data_resampling: Optional[bool] = field(
        default=False,
        metadata={'help': 'Set to True to use data resampling.'},
    )
    dynamic_image_size: Optional[bool] = field(
        default=False,
        metadata={'help': 'Set to True to use dynamic image size.'},
    )
    use_thumbnail: Optional[bool] = field(
        default=False,
        metadata={'help': 'Set to True to add a thumbnail image.'},
    )
    min_dynamic_patch: Optional[int] = field(
        default=1,
        metadata={'help': 'The minimum number of dynamic patches. Default is 1.'},
    )
    max_dynamic_patch: Optional[int] = field(
        default=12,
        metadata={'help': 'The maximum number of dynamic patches. Default is 6.'},
    )
    normalize_type: Optional[str] = field(
        default='imagenet',
        metadata={'help': 'The normalize type for the image. Default is imagenet.'},
    )
    
class SampleFrames:
    def __init__(self, clip_len, frame_interval=1, num_clips=1):

        self.clip_len = clip_len
        self.frame_interval = frame_interval
        self.num_clips = num_clips

    def _get_train_clips(self, num_frames):
        """Get clip offsets in train mode.

        It will calculate the average interval for selected frames,
        and randomly shift them within offsets between [0, avg_interval].
        If the total number of frames is smaller than clips num or origin
        frames length, it will return all zero indices.

        Args:
            num_frames (int): Total number of frame in the video.

        Returns:
            np.ndarray: Sampled frame indices in train mode.
        """
        ori_clip_len = self.clip_len * self.frame_interval
        avg_interval = (num_frames - ori_clip_len + 1) // self.num_clips

        if avg_interval > 0:
            base_offsets = np.arange(self.num_clips) * avg_interval
            clip_offsets = base_offsets + np.random.randint(
                avg_interval, size=self.num_clips
            )
        elif num_frames > max(self.num_clips, ori_clip_len):
            clip_offsets = np.sort(
                np.random.randint(num_frames - ori_clip_len + 1, size=self.num_clips)
            )
        elif avg_interval == 0:
            ratio = (num_frames - ori_clip_len + 1.0) / self.num_clips
            clip_offsets = np.around(np.arange(self.num_clips) * ratio)
        else:
            clip_offsets = np.zeros((self.num_clips,), dtype=np.int)
        return clip_offsets

    def _get_test_clips(self, num_frames, start_index=0):
        """Get clip offsets in test mode.

        Calculate the average interval for selected frames, and shift them
        fixedly by avg_interval/2.

        Args:
            num_frames (int): Total number of frame in the video.

        Returns:
            np.ndarray: Sampled frame indices in test mode.
        """
        ori_clip_len = self.clip_len * self.frame_interval
        avg_interval = (num_frames - ori_clip_len + 1) / float(self.num_clips)
        if num_frames > ori_clip_len - 1:
            base_offsets = np.arange(self.num_clips) * avg_interval
            clip_offsets = (base_offsets + avg_interval / 2.0).astype(np.int32)
        else:
            clip_offsets = np.zeros((self.num_clips,), dtype=np.int32)
        return clip_offsets

    def __call__(self, total_frames, train=False, start_index=0):
        """Perform the SampleFrames loading.

        Args:
            results (dict): The resulting dict to be modified and passed
                to the next transform in pipeline.
        """
        if train:
            clip_offsets = self._get_train_clips(total_frames)
        else:
            clip_offsets = self._get_test_clips(total_frames)
        frame_inds = (
            clip_offsets[:, None]
            + np.arange(self.clip_len)[None, :] * self.frame_interval
        )
        frame_inds = np.concatenate(frame_inds)

        frame_inds = frame_inds.reshape((-1, self.clip_len))
        frame_inds = np.mod(frame_inds, total_frames)
        frame_inds = np.concatenate(frame_inds) + start_index
        return frame_inds.astype(np.int32)
        
class LazySupervisedDataset(Dataset):
    """Dataset for supervised fine-tuning."""

    def __init__(
        self,
        template_name,
        meta,
        train_eval,
        tokenizer,
        tcs_loader,
        ds_name,
        num_image_token,
        image_size=224,
        is_train=True,
        pad2square=False,
        group_by_length=False,
        dynamic_image_size=False,
        use_thumbnail=False,
        min_dynamic_patch=1,
        max_dynamic_patch=6,
        min_num_frame=4,  # for video data
        max_num_frame=12,  # for video data
        sampling_method='rand',  # for video data
        repeat_time=1,
        normalize_type='imagenet',
        random_seed=0,
    ):
        super(LazySupervisedDataset, self).__init__()
        self.ds_name = ds_name
        self.tokenizer = tokenizer
        self.template_name = template_name
        self.num_image_token = num_image_token
        logger.info(f'[Dataset] num_image_token: {num_image_token}')
        logger.info(f'[Dataset] dynamic_image_size: {dynamic_image_size}')
        logger.info(f'[Dataset] use_thumbnail: {use_thumbnail}')
        logger.info(f'[Dataset] min_dynamic_patch: {min_dynamic_patch}, max_dynamic_patch: {max_dynamic_patch}')

        self.image_size = image_size
        self.is_train = is_train
        self.pad2square = pad2square
        self.max_num_frame = max_num_frame
        self.min_num_frame = min_num_frame
        self.sampling_method = sampling_method
        self.raw_data = []
        logger.info('Formatting inputs...Skip in lazy mode')
        self.root = meta['root']
        # print('train_eval',train_eval)

        if train_eval=='eval':
            video_name_txt = meta.get("video_name_txt")
            prompt_txt = meta.get("prompt_txt")
            video_paths_to_process = []

            # Try to read the list of video paths from the provided text file
            if video_name_txt and os.path.exists(video_name_txt):
                logger.info(f"Reading video list from: {video_name_txt}")
                try:
                    with open(video_name_txt, 'r') as f:
                        video_paths_to_process = [line.strip() for line in f if line.strip()]
                    logger.info(f"Successfully loaded {len(video_paths_to_process)} video paths from file.")
                except Exception as e:
                    logger.error(f"Failed to read {video_name_txt}: {e}. Will scan directory instead.")
                    video_paths_to_process = []  # Clear list to trigger scan
            if prompt_txt and os.path.exists(prompt_txt):
                logger.info(f"Reading prompt list from: {prompt_txt}")
                try:
                    with open(prompt_txt, 'r') as f:
                        prompts = [line.strip() for line in f if line.strip()]
                    logger.info(f"Successfully loaded {len(prompts)} prompts from file.")
                except Exception as e:
                    logger.error(f"Failed to read {prompt_txt}: {e}. Will scan directory instead.")
                    prompts = []  # Clear list to trigger scan
            # If the text file was not provided, was empty, or failed to load, scan the root directory
            # if not video_paths_to_process:
            #     logger.info(f"No valid video list file used. Scanning for .mp4 files in: {self.root}")
            #     for dirpath, _, filenames in os.walk(self.root):
            #         for filename in filenames:
            #             if filename.lower().endswith('.mp4'):
            #                 relative_path = os.path.relpath(os.path.join(dirpath, filename), self.root).replace('\\', '/')
            #                 video_paths_to_process.append(relative_path)
            #     logger.info(f"Found {len(video_paths_to_process)} videos by scanning directory.")

            # Create the raw_data list from the collected video paths
            self.raw_data = []
            for video_path, prompt in zip(video_paths_to_process, prompts):
                data_item = {
                    "video": video_path,
                    "conversations": [
                        {"from": "human", "value": f"How would you rate the correspondence of this video and its prompt? prompt:{prompt}"},
                        {"from": "gpt", "value": "The correspondence of the video and its prompt is good."}
                    ]
                }
                self.raw_data.append(json.dumps(data_item))

            if repeat_time < 1:
                # If repeat_time is less than 1, select a portion of the data
                self.raw_data = self.raw_data[:int(len(self.raw_data) * repeat_time)]
            if repeat_time > 1:
                assert isinstance(repeat_time, int)
                # Repeat the list if repeat_time is greater than 1
                self.raw_data = self.raw_data * repeat_time
                    
        # print('self.raw_data',self.raw_data)
        

        gc.collect()
        
        self.cached_data_dict = {}
        self.tcs_loader = tcs_loader
        self.group_by_length = group_by_length
        self.dynamic_image_size = dynamic_image_size
        self.use_thumbnail = use_thumbnail
        self.min_dynamic_patch = min_dynamic_patch
        self.max_dynamic_patch = max_dynamic_patch
        self.normalize_type = normalize_type
        
        self.sampler = SampleFrames(clip_len = 32, num_clips = 4)
        # If the precomputed length does not exist, roughly estimate the length of
        # each sample to improve the efficiency of group_by_length.
        if self.group_by_length:
            self.conv2length = {}  # Using a dictionary to speed up token length calculation
            self.length = []
            for data_item in self.raw_data:
                data_item = json.loads(data_item)
                # if 'length' in data_item:
                token_length = 461
                self.length.append(token_length)
        gc.collect()

    def __len__(self):
        return len(self.raw_data)

    def get_preprocess_function(self):
        # Select the appropriate preprocessing function based on the template name
        if self.template_name == 'Hermes-2':
            preprocess_function = preprocess_mpt
        elif self.template_name == 'internlm2-chat':
            preprocess_function = preprocess_internlm
        elif self.template_name == 'phi3-chat':
            preprocess_function = preprocess_phi3
        else:
            preprocess_function = preprocess
        return preprocess_function

    def load_image(self, image_path):
        # Load the image using tcs_loader if available, otherwise use PIL
        if self.tcs_loader is not None and 's3://' in image_path:
            return self.tcs_loader(image_path)
        return Image.open(image_path).convert('RGB')

    def get_image_path(self, image_path):
        if image_path.startswith('s3://'):  # for ceph
            image_path = self.root + image_path
        else:  # for local image
            image_path = os.path.join(self.root, image_path)
        return image_path

    def get_transform(self):
        # Build transformation function
        transform = build_transform(is_train=self.is_train, input_size=self.image_size,
                                    pad2square=self.pad2square, normalize_type=self.normalize_type)
        return transform
    
    def get_spatial_fragments(
        video,
        C,
        T,
        H,
        W,
        fragments_h=7,
        fragments_w=7,
        fsize_h=32,
        fsize_w=32,
        aligned=32,
        nfrags=1,
        random=False,
        random_upsample=False,
        fallback_type="upsample"
    ):
        size_h = fragments_h * fsize_h
        size_w = fragments_w * fsize_w
        ## video: [C,T,H,W]
        ## situation for images
        # if video.shape[1] == 1:
        #     aligned = 1

        dur_t, res_h, res_w = T, H, W
        ratio = min(res_h / size_h, res_w / size_w)
        if fallback_type == "upsample" and ratio < 1:
            
            ovideo = video
            video = torch.nn.functional.interpolate(
                video / 255.0, scale_factor=1 / ratio, mode="bilinear"
            )
            video = (video * 255.0).type_as(ovideo)
            
        if random_upsample:

            randratio = random.random() * 0.5 + 1
            video = torch.nn.functional.interpolate(
                video / 255.0, scale_factor=randratio, mode="bilinear"
            )
            video = (video * 255.0).type_as(ovideo)



        assert dur_t % aligned == 0, "Please provide match vclip and align index"
        size = size_h, size_w

        ## make sure that sampling will not run out of the picture
        hgrids = torch.LongTensor(
            [min(res_h // fragments_h * i, res_h - fsize_h) for i in range(fragments_h)]
        )
        wgrids = torch.LongTensor(
            [min(res_w // fragments_w * i, res_w - fsize_w) for i in range(fragments_w)]
        )
        hlength, wlength = res_h // fragments_h, res_w // fragments_w

        if random:
            print("This part is deprecated. Please remind that.")
            if res_h > fsize_h:
                rnd_h = torch.randint(
                    res_h - fsize_h, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_h = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()
            if res_w > fsize_w:
                rnd_w = torch.randint(
                    res_w - fsize_w, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_w = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()
        else:
            if hlength > fsize_h:
                rnd_h = torch.randint(
                    hlength - fsize_h, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_h = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()
            if wlength > fsize_w:
                rnd_w = torch.randint(
                    wlength - fsize_w, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_w = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()

        target_video = torch.zeros([H,W] + size).to(video.device)
        # target_videos = []

        for i, hs in enumerate(hgrids):
            for j, ws in enumerate(wgrids):
                for t in range(dur_t // aligned):
                    t_s, t_e = t * aligned, (t + 1) * aligned
                    h_s, h_e = i * fsize_h, (i + 1) * fsize_h
                    w_s, w_e = j * fsize_w, (j + 1) * fsize_w
                    if random:
                        h_so, h_eo = rnd_h[i][j][t], rnd_h[i][j][t] + fsize_h
                        w_so, w_eo = rnd_w[i][j][t], rnd_w[i][j][t] + fsize_w
                    else:
                        h_so, h_eo = hs + rnd_h[i][j][t], hs + rnd_h[i][j][t] + fsize_h
                        w_so, w_eo = ws + rnd_w[i][j][t], ws + rnd_w[i][j][t] + fsize_w
                    target_video[:, t_s:t_e, h_s:h_e, w_s:w_e] = video[
                        :, t_s:t_e, h_so:h_eo, w_so:w_eo
                    ]
        # target_videos.append(video[:,t_s:t_e,h_so:h_eo,w_so:w_eo])
        # target_video = torch.stack(target_videos, 0).reshape((dur_t // aligned, fragments, fragments,) + target_videos[0].shape).permute(3,0,4,1,5,2,6)
        # target_video = target_video.reshape((-1, dur_t,) + size) ## Splicing Fragments
        return target_video
    def get_index(self, bound, fps, max_frame, first_idx, num_segments):
        if bound:
            start, end = bound[0], bound[1]
        else:
            start, end = -100000, 100000
        start_idx = max(first_idx, round(start * fps))
        end_idx = min(round(end * fps), max_frame)
        seg_size = float(end_idx - start_idx) / num_segments
        frame_indices = np.array([
            int(start_idx + (seg_size / 2) + np.round(seg_size * idx))
            for idx in range(num_segments)
        ])
        return frame_indices
    def load_video(self, video_path, bound=None, input_size=448, max_num=1, num_segments=8):
        from decord import VideoReader, cpu
        vr = VideoReader(video_path, ctx=cpu(0), num_threads=1)
        max_frame = len(vr) - 1
        fps = float(vr.get_avg_fps())

        pixel_values_list = []
        frame_indices = self.get_index(bound, fps, max_frame, first_idx=0, num_segments=num_segments)
        for frame_index in frame_indices:
            img = Image.fromarray(vr[frame_index].asnumpy()).convert('RGB')
            img = dynamic_preprocess(img, image_size=input_size, use_thumbnail=True, max_num=max_num)
            pixel_values_list.append(img[0])
        return pixel_values_list
        # return img
        
    def load_video_fast(self, video_path):
        from decord import VideoReader, cpu
        video_reader = VideoReader(video_path)
        frames = self.sampler(len(video_reader))
        # print("Sampled frames are", frames)
        frame_dict = {idx: video_reader[idx].asnumpy() for idx in np.unique(frames)}
        imgs = [torch.from_numpy(frame_dict[idx]) for idx in frames]
        video = torch.stack(imgs, 0)
        video = video.permute(3, 0, 1, 2)
        dur_t, res_h, res_w = video.shape[-3:]
        fragments_h=7
        fragments_w=7
        fsize_h=32
        fsize_w=32
        aligned=32
        nfrags=1
        random=False
        random_upsample=False
        size_h = fragments_h * fsize_h
        size_w = fragments_w * fsize_w
        ratio = min(res_h / size_h, res_w / size_w)
        fallback_type="upsample"
        if fallback_type == "upsample" and ratio < 1:
            
            ovideo = video
            video = torch.nn.functional.interpolate(
                video / 255.0, scale_factor=1 / ratio, mode="bilinear"
            )
            video = (video * 255.0).type_as(ovideo)
            
        if random_upsample:

            randratio = random.random() * 0.5 + 1
            video = torch.nn.functional.interpolate(
                video / 255.0, scale_factor=randratio, mode="bilinear"
            )
            video = (video * 255.0).type_as(ovideo)



        assert dur_t % aligned == 0, "Please provide match vclip and align index"
        size = size_h, size_w

        ## make sure that sampling will not run out of the picture
        hgrids = torch.LongTensor(
            [min(res_h // fragments_h * i, res_h - fsize_h) for i in range(fragments_h)]
        )
        wgrids = torch.LongTensor(
            [min(res_w // fragments_w * i, res_w - fsize_w) for i in range(fragments_w)]
        )
        hlength, wlength = res_h // fragments_h, res_w // fragments_w

        if random:
            print("This part is deprecated. Please remind that.")
            if res_h > fsize_h:
                rnd_h = torch.randint(
                    res_h - fsize_h, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_h = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()
            if res_w > fsize_w:
                rnd_w = torch.randint(
                    res_w - fsize_w, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_w = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()
        else:
            if hlength > fsize_h:
                rnd_h = torch.randint(
                    hlength - fsize_h, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_h = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()
            if wlength > fsize_w:
                rnd_w = torch.randint(
                    wlength - fsize_w, (len(hgrids), len(wgrids), dur_t // aligned)
                )
            else:
                rnd_w = torch.zeros((len(hgrids), len(wgrids), dur_t // aligned)).int()

        target_video = torch.zeros(video.shape[:-2] + size)
        # target_videos = []

        for i, hs in enumerate(hgrids):
            for j, ws in enumerate(wgrids):
                for t in range(dur_t // aligned):
                    t_s, t_e = t * aligned, (t + 1) * aligned
                    h_s, h_e = i * fsize_h, (i + 1) * fsize_h
                    w_s, w_e = j * fsize_w, (j + 1) * fsize_w
                    if random:
                        h_so, h_eo = rnd_h[i][j][t], rnd_h[i][j][t] + fsize_h
                        w_so, w_eo = rnd_w[i][j][t], rnd_w[i][j][t] + fsize_w
                    else:
                        h_so, h_eo = hs + rnd_h[i][j][t], hs + rnd_h[i][j][t] + fsize_h
                        w_so, w_eo = ws + rnd_w[i][j][t], ws + rnd_w[i][j][t] + fsize_w
                    target_video[:, t_s:t_e, h_s:h_e, w_s:w_e] = video[
                        :, t_s:t_e, h_so:h_eo, w_so:w_eo
                    ]
        
        # print(video.shape)
        sampled_video = target_video
        mean, std = torch.FloatTensor([123.675, 116.28, 103.53]), torch.FloatTensor([58.395, 57.12, 57.375])
        sampled_video = ((sampled_video.permute(1, 2, 3, 0) - mean) / std).permute(3, 0, 1, 2)
        sampled_video = sampled_video.reshape(sampled_video.shape[0], 4, -1, *sampled_video.shape[2:]).transpose(0,1)
        # vsamples[sample_type] = sampled_video.to(device)
        # print('sample_type',sample_type)
        # print('vsampled_video',sampled_video.shape)
        return sampled_video
    def load_video2(self, video_path, bound=None, input_size=448, max_num=1, num_segments=8):
        from decord import VideoReader, cpu
        vr = VideoReader(video_path, ctx=cpu(0), num_threads=1)
        max_frame = len(vr) - 1
        fps = float(vr.get_avg_fps())

        pixel_values_list = []
        if len(vr)<32:
            num_segments =32
        else:
            num_segments=len(vr)
        frame_indices = self.get_index(bound, fps, max_frame, first_idx=0, num_segments=num_segments)
        for frame_index in frame_indices:
            img = Image.fromarray(vr[frame_index].asnumpy()).convert('RGB')
            img = dynamic_preprocess(img, image_size=input_size, use_thumbnail=True, max_num=max_num)
            pixel_values_list.append(img[0])
        return pixel_values_list
    def video_get_item(self, data_item):
        # Build transformation function
        transform = self.get_transform()

        # Ensure the first conversation contains a video placeholder
        if '<video>' not in data_item['conversations'][0]['value']:
            data_item['conversations'][0]['value'] = '<video>\n' + data_item['conversations'][0]['value']

        # Get the video file path
        video_file = data_item['video']
        video_name = data_item['video']
        video_path = os.path.join(self.root, video_file)
        # Load the video frames using tcs_loader
        # TODO: Load videos without using tcsloader.
        sampled_video = self.load_video_fast(video_path)
        image_list = self.load_video(video_path)
        # image_list2 = self.load_video2(video_path)
        
        # Generate special tokens for each video frame
        special_tokens = '\n'.join(['Frame{}: <image>'.format(i + 1) for i in range(len(image_list))])
        special_tokens = special_tokens + '\nMotion Feature: <image><image><image><image>'+ '\nMotion Feature2: <image>'
        
        
        # print(special_tokens)
        data_item['conversations'][0]['value'] = data_item['conversations'][0]['value'].replace(
            '<video>\n', special_tokens)

        # Transform each frame image and stack them into a tensor
        pixel_values = [transform(image) for image in image_list]
        pixel_values = torch.stack(pixel_values)
        # pixel_values3 = [transform(image) for image in image_list2]
        # pixel_values3 = torch.stack(pixel_values3)
        
        num_patches = pixel_values.size(0) + 4

        # Select the appropriate preprocessing function based on the template name
        preprocess_function = self.get_preprocess_function()

        # Preprocess the conversations and generate the return dictionary
        num_image_tokens = [self.num_image_token] * num_patches
        # print('num_image_tokens',num_image_tokens)
        num_image_tokens[-4:-1] = [1,1,1,1]
        
      
        ret = preprocess_function(self.template_name, [deepcopy(data_item['conversations'])],
                                  self.tokenizer, num_image_tokens, group_by_length=self.group_by_length,
                                  ds_name=self.ds_name, num_image=num_patches)
        # print('pixel_values',pixel_values.shape)
        # Create the final return dictionary
        # mos = torch.tensor(float(data_item['mos'])/100, dtype=torch.bfloat16)
        # answer = data_item['conversations'][1]['value']
        # Create the final return dictionary
        ret = dict(
            video_name = video_name,
            input_ids=ret['input_ids'][0],
            labels=ret['labels'][0],
            attention_mask=ret['attention_mask'][0],
            pixel_values=pixel_values,
            pixel_values2=sampled_video,
            # pixel_values3=pixel_values3,
            image_flags=torch.tensor([1] * (num_patches-4), dtype=torch.long)
        )
        return ret

    def pure_text_get_item(self, data_item):
        # Build transformation function
        transform = self.get_transform()

        # Create a blank white image
        image = Image.new('RGB', (224, 224), (255, 255, 255))

        # Dynamically preprocess the image to generate patches
        images = dynamic_preprocess(image, min_num=self.min_dynamic_patch, max_num=1,
                                    image_size=self.image_size, use_thumbnail=self.use_thumbnail)

        # Apply the transformation to each image patch and stack them into a tensor
        pixel_values = [transform(image) for image in images]
        pixel_values = torch.stack(pixel_values)
        num_patches = pixel_values.size(0) + 1

        # Ensure there is only one patch
        assert num_patches == 1, f'The number of patches should be 1, but got {num_patches}.'

        # Select the appropriate preprocessing function based on the template name
        preprocess_function = self.get_preprocess_function()

        # Preprocess the conversations and generate the return dictionary
        ret = preprocess_function(self.template_name, [deepcopy(data_item['conversations'])],
                                  self.tokenizer, [self.num_image_token * num_patches], text_only=True,
                                  group_by_length=self.group_by_length, ds_name=self.ds_name)

        # Create the final return dictionary
        ret = dict(
            input_ids=ret['input_ids'][0],
            labels=ret['labels'][0],
            attention_mask=ret['attention_mask'][0],
            pixel_values=pixel_values,
            image_flags=torch.tensor([0] * num_patches, dtype=torch.long)
        )
        return ret

    def __getitem__(self, i) -> Dict[str, torch.Tensor]:
        i = i % len(self.raw_data)
        while True:
            try:
                data_item = json.loads(self.raw_data[i])
                if 'image' in data_item and len(data_item['image']) != 0:
                    if type(data_item['image']) == list:
                        ret = self.multi_modal_multi_image_get_item(data_item)
                    else:
                        ret = self.multi_modal_get_item(data_item)
                elif 'video' in data_item and data_item['video'] is not None and data_item['video'] != '':
                    ret = self.video_get_item(data_item)
                else:
                    ret = self.pure_text_get_item(data_item)
                break
            except Exception as e:
                print(e, self.ds_name, flush=True)
                if not isinstance(e, UnidentifiedImageError):
                    traceback.print_exc()
                data_item = json.loads(self.raw_data[i])
                if 'image' in data_item:
                    if type(data_item['image']) == list:
                        images = [self.root + item for item in data_item['image']]
                        print(f'Failed to load image: {images}, the dataset is: {self.ds_name}')
                    else:
                        if data_item['image'].startswith('s3://'):
                            data_path = self.root + data_item['image']
                        else:
                            data_path = os.path.join(self.root, data_item['image'])
                        print(f'Failed to load image: {data_path}, the dataset is: {self.ds_name}')
                elif 'video' in data_item:
                    data_path = os.path.join(self.root, data_item['video'])
                    print(f'Failed to load video: {data_path}, the dataset is: {self.ds_name}')
                i = random.randint(0, len(self.raw_data) - 1)
        return ret
import pandas as pd
from scipy.stats import spearmanr, pearsonr, kendalltau
def save_and_evaluate(data_list, output_file='results.csv', metrics_file='metrics.txt'):
    # Convert the list into a pandas DataFrame
    df = pd.DataFrame(data_list, columns=['video_name', 'pred_score'])
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f'Results saved to {output_file}')
    # Calculate SRCC, PLCC, KRCC
    
  
def build_datasets(
    data_args,
    train_eval,
    tokenizer,
    tcs_loader,
    model,
    group_by_length=False,
    dynamic_image_size=False,
    use_thumbnail=False,
    min_dynamic_patch=1,
    max_dynamic_patch=12,
    normalize_type='imagenet',
):
    datasets = []
    lengths = []
    ds_collections = json.loads(open(data_args.meta_path).read())
    for ds_idx, ds_name in enumerate(ds_collections.keys()):
        repeat_time = ds_collections[ds_name]['repeat_time']
        if 'max_dynamic_patch' in ds_collections[ds_name]:
            max_num = ds_collections[ds_name]['max_dynamic_patch']
            logger.info(f'max_dynamic_patch is set to {max_num} according to the meta file')
        else:
            max_num = max_dynamic_patch
        dataset = LazySupervisedDataset(
            data_args.conv_style, ds_collections[ds_name],train_eval,
            tokenizer,
            tcs_loader,
            ds_name=ds_name,
            num_image_token=model.num_image_token,
            image_size=data_args.force_image_size,
            is_train=ds_collections[ds_name]['data_augment'],
            pad2square=data_args.pad2square,
            group_by_length=group_by_length,
            dynamic_image_size=dynamic_image_size,
            use_thumbnail=use_thumbnail,
            min_dynamic_patch=min_dynamic_patch,
            max_dynamic_patch=max_num,
            repeat_time=repeat_time,
            normalize_type=normalize_type,
            random_seed=ds_idx,
        )
        logger.info(f'Add dataset: {ds_name} with length: {len(dataset)}')
        datasets.append(dataset)
        if data_args.use_data_resampling:
            lengths.append(math.sqrt(len(dataset)))
        else:
            lengths.append(len(dataset))
    if data_args.use_data_resampling:
        total_length = sum(lengths)
        weights = [l / total_length for l in lengths]
        train_dataset = WeightedConcatDataset(datasets, weights)
    else:
        train_dataset = ConcatDataset(datasets)
    return train_dataset
def load_lora_weights(model, lora_weight_path):
    lora_state_dict = torch.load(lora_weight_path)
    model.load_state_dict(lora_state_dict, strict=False)
    logger.info(f'Loaded LoRA weights from {lora_weight_path}')

def main():
    # Parse input arguments
    # See all possible arguments in src/transformers/training_args.py
    # If use DeepSpeed zero3, init_dist must before HfArgumentParser
    launcher = os.environ.get('LAUNCHER', 'slurm')
    init_dist(launcher=launcher, backend='nccl')
    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments, CustomArguments))
    if len(sys.argv) == 2 and sys.argv[1].endswith('.json'):
        # If we pass only one argument to the script, and it's the path to a json file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args, custom_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))
    else:
        model_args, data_args, training_args, custom_args = parser.parse_args_into_dataclasses()
    training_args.evaluation_strategy = "steps"
    training_args.do_eval =True
    training_args.per_device_eval_batch_size =1
    # Sending telemetry. Tracking the example usage helps us better allocate resources to maintain them. The
    # information sent is the one passed as arguments along with your Python/PyTorch versions.
    # send_example_telemetry('InternV-Chat', model_args, data_args)

    # Setup logging
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S',
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    if training_args.should_log:
        # The default of training_args.log_level is passive, so we set log level at info here to have that default.
        transformers.utils.logging.set_verbosity_info()

    log_level = training_args.get_process_log_level()
    logger.setLevel(log_level)
    set_verbosity(log_level)
    enable_default_handler()
    enable_explicit_format()

    # Log on each process the small summary:
    logger.warning(
        f'Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}'
        + f'distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}'
    )
    logger.info(f'Training/evaluation parameters {training_args}')

    # Detecting last checkpoint and eventually continue from last checkpoint.
    last_checkpoint = None
    if os.path.isdir(training_args.output_dir) and training_args.do_train and not training_args.overwrite_output_dir:
        last_checkpoint = get_last_checkpoint(training_args.output_dir)
        if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
            raise ValueError(
                f'Output directory ({training_args.output_dir}) already exists and is not empty. '
                'Use --overwrite_output_dir to overcome.'
            )
        elif last_checkpoint is not None and training_args.resume_from_checkpoint is None:
            logger.info(
                f'Checkpoint detected, resuming training at {last_checkpoint}. To avoid this behavior, change '
                'the `--output_dir` or add `--overwrite_output_dir` to train from scratch.'
            )
    # Set seed before initializing model.
    set_seed(training_args.seed)

    # Load pretrained model, tokenizer, and image processor
    tokenizer_path = model_args.model_name_or_path or model_args.llm_path
    logger.info(f'Loading Tokenizer: {tokenizer_path}')
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_path, add_eos_token=False, trust_remote_code=True, use_fast=False)
    tokenizer.tokenizer_path = tokenizer_path
    tokenizer.model_max_length = data_args.max_seq_length
    token_list = [IMG_START_TOKEN, IMG_END_TOKEN, IMG_CONTEXT_TOKEN,
                  QUAD_START_TOKEN, QUAD_END_TOKEN, REF_START_TOKEN,
                  REF_END_TOKEN, BOX_START_TOKEN, BOX_END_TOKEN]
    num_new_tokens = tokenizer.add_tokens(token_list, special_tokens=True)
    img_context_token_id = tokenizer.convert_tokens_to_ids(IMG_CONTEXT_TOKEN)
    tcs_loader = TCSLoader('~/petreloss.conf') if has_tcs_loader else None

    if model_args.model_name_or_path is not None:
        logger.info('Loading InternVLChatModel...')
        config = InternVLChatConfig.from_pretrained(model_args.model_name_or_path)
        config.vision_config.drop_path_rate = model_args.drop_path_rate
        if config.llm_config.model_type == 'internlm2':
            config.llm_config.attn_implementation = 'flash_attention_2'  # for InternLM
            logger.info('Using flash_attention_2 for InternLM')
        else:
            config.llm_config._attn_implementation = 'flash_attention_2'  # for LLaMA
            logger.info('Using flash_attention_2 for LLaMA')
        config.template = data_args.conv_style
        config.select_layer = model_args.vision_select_layer
        config.dynamic_image_size = data_args.dynamic_image_size
        config.use_thumbnail = data_args.use_thumbnail
        config.ps_version = model_args.ps_version
        config.min_dynamic_patch = data_args.min_dynamic_patch
        config.max_dynamic_patch = data_args.max_dynamic_patch
        model = InternVLChatModel.from_pretrained(
            model_args.model_name_or_path, torch_dtype=torch.bfloat16, config=config)
        if os.path.exists(os.path.join(model_args.model_name_or_path,"lora_weights.pth")):
            lora_weight_path = os.path.join(model_args.model_name_or_path,"lora_weights.pth")
            load_lora_weights(model, lora_weight_path)  # Add this line to load LoRA weights
    else:
        logger.info('Loading ViT-6B...')
        vision_config = InternVisionConfig.from_pretrained(model_args.vision_path)
        vision_config.drop_path_rate = model_args.drop_path_rate
        vision_model = InternVisionModel.from_pretrained(
            model_args.vision_path, torch_dtype=torch.bfloat16, config=vision_config)
        logger.info('Loading LLaMA...')
        llm_config = AutoConfig.from_pretrained(model_args.llm_path, trust_remote_code=True)
        if llm_config.model_type == 'internlm2':
            model_type = InternLM2ForCausalLM
            llm_config.attn_implementation = 'flash_attention_2'  # for InternLM
            logger.info('Using flash_attention_2 for InternLM')
        else:
            model_type = AutoModelForCausalLM
            llm_config._attn_implementation = 'flash_attention_2'  # for LLaMA
            logger.info('Using flash_attention_2 for LLaMA')
        llm = model_type.from_pretrained(
            model_args.llm_path, torch_dtype=torch.bfloat16,
            config=llm_config, trust_remote_code=True)
        logger.info('Building InternVLChatConfig...')
        internvl_chat_config = InternVLChatConfig(
            vision_config.to_dict(), llm_config.to_dict(), downsample_ratio=data_args.down_sample_ratio,
            pad2square=data_args.pad2square, template=data_args.conv_style,
            select_layer=model_args.vision_select_layer, dynamic_image_size=data_args.dynamic_image_size,
            use_thumbnail=data_args.use_thumbnail, ps_version=model_args.ps_version,
            min_dynamic_patch=data_args.min_dynamic_patch, max_dynamic_patch=data_args.max_dynamic_patch)
        internvl_chat_config.force_image_size = data_args.force_image_size
        logger.info('Building InternVLChatModel...')
        model = InternVLChatModel(internvl_chat_config, vision_model, llm)
    model.img_context_token_id = img_context_token_id

    assert model.config.downsample_ratio == data_args.down_sample_ratio

    if model_args.mlp_path is not None:
        logger.info('Loading pretrained MLP projector...')
        state_dict = torch.load(model_args.mlp_path, map_location='cpu')
        message = model.mlp1.load_state_dict(state_dict)
        logger.info(message)
    logger.info('Finished')

    patch_size = model.config.vision_config.patch_size
    logger.info(f'model.config.force_image_size: {model.config.force_image_size}')
    logger.info(f'data_args.force_image_size: {data_args.force_image_size}')
    logger.info(f'model.config.vision_config.image_size: {model.config.vision_config.image_size}')
    if model.config.vision_config.image_size != data_args.force_image_size:
        logger.info(f'Resizing position embedding from '
                    f'{model.config.vision_config.image_size} '
                    f'to {data_args.force_image_size}...')
        model.vision_model.resize_pos_embeddings(old_size=model.config.vision_config.image_size,
                                                 new_size=data_args.force_image_size,
                                                 patch_size=patch_size)
        model.config.vision_config.image_size = data_args.force_image_size
    model.config.force_image_size = data_args.force_image_size
    model.num_image_token = int((data_args.force_image_size // patch_size) ** 2 * (data_args.down_sample_ratio ** 2))

    if num_new_tokens > 0:
        model.language_model.resize_token_embeddings(len(tokenizer))
        output_embeddings = model.language_model.get_output_embeddings().weight.data
        output_embeddings_avg = output_embeddings[:-num_new_tokens].mean(dim=0, keepdim=True)
        output_embeddings[-num_new_tokens:] = output_embeddings_avg

        model.config.llm_config.vocab_size = len(tokenizer)
        model.language_model.config.vocab_size = len(tokenizer)

    model.language_model.config.use_cache = False
    model.vision_model.gradient_checkpointing = True
    model.vision_model.encoder.gradient_checkpointing = True
    if model_args.grad_checkpoint:
        model.language_model._set_gradient_checkpointing()

    # train_dataset = build_datasets(
    #     data_args, 'train', tokenizer, tcs_loader, model, group_by_length=training_args.group_by_length,
    #     dynamic_image_size=data_args.dynamic_image_size, use_thumbnail=data_args.use_thumbnail,
    #     min_dynamic_patch=data_args.min_dynamic_patch, max_dynamic_patch=data_args.max_dynamic_patch,
    #     normalize_type=data_args.normalize_type)
    eval_dataset = build_datasets(
        data_args, 'eval', tokenizer, tcs_loader, model, group_by_length=training_args.group_by_length,
        dynamic_image_size=data_args.dynamic_image_size, use_thumbnail=data_args.use_thumbnail,
        min_dynamic_patch=data_args.min_dynamic_patch, max_dynamic_patch=data_args.max_dynamic_patch,
        normalize_type=data_args.normalize_type)
    print('eval_dataset',eval_dataset)
    def _freeze_params(module):
        for param in module.parameters():
            param.requires_grad = False

    if model_args.freeze_backbone:
        # model.vision_model = model.vision_model.eval()
        _freeze_params(model.vision_model)
        _freeze_params(model.evaluator)
   

    if model_args.freeze_llm:
        model.language_model = model.language_model.eval()
        _freeze_params(model.language_model)
       

    if model_args.unfreeze_lm_head:
        model.language_model.lm_head.requires_grad = True

    if model_args.use_backbone_lora:
        model.wrap_backbone_lora(r=model_args.use_backbone_lora, lora_alpha=2 * model_args.use_backbone_lora)
        model.config.use_backbone_lora = model_args.use_backbone_lora

    if model_args.use_llm_lora:
        model.wrap_llm_lora(r=model_args.use_llm_lora, lora_alpha=2 * model_args.use_llm_lora)
        model.config.use_llm_lora = model_args.use_llm_lora

    if model_args.freeze_mlp:
        _freeze_params(model.mlp1)
        _freeze_params(model.fast_mlp)
       


    if model_args.unfreeze_vit_layers != 0:
        layers = model.vision_model.encoder.layers[model_args.unfreeze_vit_layers:]
        for k, v in layers.named_parameters():
            logger.info(f'Unfreezing ViT layer: {k}')
            v.requires_grad = True

    # print trainable parameters
    if dist.get_rank() == 0:
        for name, param in model.named_parameters():
            if param.requires_grad:
                logger.info(name)

    # set seed for torch dataloaders
    set_seed(training_args.seed)

    # Initialize our Trainer
    if model_args.use_custom_trainer:
        replace_create_optimizer()
  
    # Initialize our Trainer
    from torch.utils.data import DataLoader
    
    model.eval()
    model.cuda()
    test_dataloader = DataLoader(
        eval_dataset,
        batch_size=1
    )

    
    data_list = []
    with torch.no_grad():
        for item2 in tqdm(test_dataloader, desc="Evaluating"):
            item = {}
            for k, v in item2.items():
                if k!='video_name' and k!='answer':
                    item[k] = v.to(model.device)
            # Get video name
            video_name = item2['video_name'][0]  # Assuming video name is part of the data
            # answer = item2['answer'][0]
            print(video_name)
            # Get MOS score
            
            # Forward pass
            output =  model(
                # mos=item["mos"][0].to(torch.bfloat16),
                pixel_values=item["pixel_values"][0].to(torch.bfloat16),
                pixel_values2=item["pixel_values2"][0].to(torch.bfloat16),
                input_ids=item["input_ids"],
                attention_mask=item["attention_mask"],
                image_flags=item["image_flags"][0],
                labels=item["labels"]
            )
            score1 = output['score1'].item()
            print('pred_score',score1)
            filtered_list = [x for x in output['label'] if x != IGNORE_INDEX and x!=IGNORE_INDEX2]
            output = tokenizer.decode(output['logit'][-len(filtered_list)-1:-1])
            
            
            data_list.append([video_name,  score1])

    # Save results to CSV and calculate SRCC, PLCC, KRCC
    output_file=custom_args.output_file
    metrics_file=custom_args.metrics_file
    save_and_evaluate(data_list, output_file=output_file, metrics_file=metrics_file)
        
    


if __name__ == '__main__':
    main()
