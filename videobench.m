clc
clear all
Path = 'E:\AIGV60K\MATLAB_handcrafted\MY\';
addpath([Path, 'NRIQA\'])
addpath([Path, 'NRIQA\BMPRI'])
addpath([Path, 'NRIQA\BPRI'])
addpath([Path, 'NRIQA\BRISQUE'])
addpath([Path, 'NRIQA\HOSA_release_v0'])
addpath([Path, 'NRIQA\NIQE'])
addpath([Path, 'NRIQA\QAC'])
addpath('YUVtoolbox\')
DatabasePath = 'E:\AIGV60K\Videos300\';
disNames = textread('E:\AIGV60K\video300.txt','%s')
brisque_feat = [];
CORNIA_feat = [];
RAPIQUE_feat = [];
TLVQM_feat = [];
bliinds_feat = [];
VIDEVAL_feat = [];
length(disNames)
for index = 1:length(disNames)
    index
    name = split(disNames{index,1},'.');
    videoname = [strcat(DatabasePath, disNames{index,1}(1:end-4), '.mp4')];
    disID = VideoReader(videoname);
    frameNum = disID.NumberOfFrames;

    vfeat = []; % brisque
    allFrame = []; % CORNIAm 
    allFrame_BLIINDS = []; % BLIINDS
    pano_BMPRI = [];
    pano_BPRI = [];
    pano_BRISQUE = [];
    pano_HOSA=[];
    pano_NIQE=[];
    pano_QAC = [];
    % for iFrame=1:frameNum
    frameInterval = floor((frameNum-1) / 7);  % 7是因为我们要采样8帧，间隔数=帧数-1
% 均匀采样8帧
    for iFrame = 1:8
        frame_idx = 1 + (iFrame-1) * frameInterval;
    % for iFrame=floor(frameNum/2)-3:floor(frameNum/2)+4
        cnt = frame_idx;
        %% MP4格式方法
        frame = read(disID,iFrame);
        Img = frame;
        img = Img;
        img_gray = rgb2gray(Img);
        pano_BMPRI(cnt,:) = BMPRI(img);
        pano_BPRI(cnt,:) = BPRI(img);
        % pano_BPRI_PSS(cnt,:) = PSS(img);
        % pano_BPRI_LSSs(cnt,:) = LSSs(img);
        % pano_BPRI_LSSn(cnt,:) = LSSn(img);
        [pano_BRISQUE(cnt,:), feature_BRISQUE(cnt,:)] = calcBRISQUE(img);
        pano_HOSA(cnt,:) = calcHOSA(img);
        pano_NIQE(cnt,:) = calcNIQE(img);
        pano_QAC(cnt,:) = calcQAC(img);
        pano_BMPRI(cnt,:) = BMPRI(img);
        pano_BPRI(cnt,:) = BPRI(img);
        % brisque
        % [pano_BRISQUE(iFrame,:), feature_BRISQUE(iFrame,:)] = calcBRISQUE(GRAYimdist);
        % bfeature = brisque_feature(double(GRAYimdist));
        % vfeat(end+1,:) = bfeature;
    end
    BRISQUEall(index,:) = mean(pano_BRISQUE);
    BMPRIall(index,:) = mean(pano_BMPRI);
    BPRIall(index,:) = mean(pano_BPRI);
    HOSAall(index,:) = mean(pano_HOSA);
    NIQEall(index,:) = mean(pano_NIQE);
    QACall(index,:) = mean(pano_QAC);

end