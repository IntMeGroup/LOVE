% -------------------------------------------------------------------------
% calculate NR-IQA of panoramic images
% -------------------------------------------------------------------------
clear all

%% add the path of NR-IQA
Path = 'E:\paper\NRIQA\';
addpath([Path, 'NRIQA\'])
addpath([Path, 'NRIQA\ARISM\'])
addpath([Path, 'NRIQA\BIQI_release'])
addpath([Path, 'NRIQA\BLIINDS2'])
addpath([Path, 'NRIQA\BMPRI'])
addpath([Path, 'NRIQA\BPRI'])
addpath([Path, 'NRIQA\BRISQUE'])
addpath([Path, 'NRIQA\CORNIA_release'])
addpath([Path, 'NRIQA\DIIVINE'])
addpath([Path, 'NRIQA\dipIQ'])
addpath([Path, 'NRIQA\FISBLIM'])
addpath([Path, 'NRIQA\GMLF'])
addpath([Path, 'NRIQA\HOSA_release_v0'])
addpath([Path, 'NRIQA\ILNIQE'])
addpath([Path, 'NRIQA\LPSI_release'])
addpath([Path, 'NRIQA\NFERM'])
addpath([Path, 'NRIQA\NFSDM'])
addpath([Path, 'NRIQA\NIQE'])
addpath([Path, 'NRIQA\PSIM'])
addpath([Path, 'NRIQA\QAC'])
addpath([Path, 'NRIQA\SISBLIM'])
addpath([Path, 'NRIQA\VideoBLIINDS'])
addpath([Path, 'NRIQA\VIIDEO_release'])

%% Path of images
ImgPath1 = 'F:\Img_score\img_project\Controlnet\';
ImgPath2 = 'F:\Img_score\img_project\DALLE\';
ImgPath3 = 'F:\Img_score\img_project\Glide\';
ImgPath4 = 'F:\Img_score\img_project\Lafite\';
ImgPath5 = 'F:\Img_score\img_project\stable-diffusion\';
ImgPath6 = 'F:\Img_score\img_project\Unidiffuser\';
ImgNumber = 400;
% distortion
for i = 1:ImgNumber
%     if mod(i-1,20)<5
     tmp=i-1;
     k=floor(tmp/4);
     t=mod(tmp,4)+1;
     if (k<10) 
        ImgName{i,1} = ['00',num2str(k),'-',num2str(t),'.png'];
     elseif(k<100)
        ImgName{i,1} = ['0',num2str(k),'-',num2str(t),'.png'];
     end
%     else
%         ImgName{i,1} = ['img',num2str(i),'.bmp'];
%     end
end

%% Calculate all NR-IQA algorithms
for cnt = 1:ImgNumber
  
    
    Img1 = imread([ImgPath1 ImgName{cnt,1}]);
    Img2 = imread([ImgPath2 ImgName{cnt,1}]);
    Img3 = imread([ImgPath3 ImgName{cnt,1}]);
    Img4 = imread([ImgPath4 ImgName{cnt,1}]);
    Img5 = imread([ImgPath5 ImgName{cnt,1}]);
    Img6 = imread([ImgPath6 ImgName{cnt,1}]);
    img = Img1;
    img_gray = rgb2gray(Img1);
%%       
%      pano_BMPRI(cnt,:) = BMPRI(Img1);%y
%      pano_BMPRI(cnt+400,:) = BMPRI(Img2);
%      pano_BMPRI(cnt+800,:) = BMPRI(Img3);
%      pano_BMPRI(cnt+1200,:) = BMPRI(Img4);
%      pano_BMPRI(cnt+1600,:) = BMPRI(Img5);
%      pano_BMPRI(cnt+2000,:) = BMPRI(Img6);
%%
%      pano_BPRI(cnt,:) = BPRI(Img1);%y
%      pano_BPRI(cnt+400,:) = BPRI(Img2);
%      pano_BPRI(cnt+800,:) = BPRI(Img3);
%      pano_BPRI(cnt+1200,:) = BPRI(Img4);
%      pano_BPRI(cnt+1600,:) = BPRI(Img5);
%      pano_BPRI(cnt+2000,:) = BPRI(Img6);
%%
%      pano_BPRI_PSS(cnt,:) = PSS(Img1);%y
%      pano_BPRI_PSS(cnt+400,:) = PSS(Img2);
%      pano_BPRI_PSS(cnt+800,:) = PSS(Img3);
%      pano_BPRI_PSS(cnt+1200,:) = PSS(Img4);
%      pano_BPRI_PSS(cnt+1600,:) = PSS(Img5);
%      pano_BPRI_PSS(cnt+2000,:) = PSS(Img6);
%%
%      pano_BPRI_LSSs(cnt,:) = LSSs(Img1);%y
%      pano_BPRI_LSSs(cnt+400,:) = LSSs(Img2);
%      pano_BPRI_LSSs(cnt+800,:) = LSSs(Img3);
%      pano_BPRI_LSSs(cnt+1200,:) = LSSs(Img4);
%      pano_BPRI_LSSs(cnt+1600,:) = LSSs(Img5);
%      pano_BPRI_LSSs(cnt+2000,:) = LSSs(Img6);
%%
%      pano_BPRI_LSSn(cnt,:) = LSSn(Img1);%y
%      pano_BPRI_LSSn(cnt+400,:) = LSSn(Img2);
%      pano_BPRI_LSSn(cnt+800,:) = LSSn(Img3);
%      pano_BPRI_LSSn(cnt+1200,:) = LSSn(Img4);
%      pano_BPRI_LSSn(cnt+1600,:) = LSSn(Img5);
%      pano_BPRI_LSSn(cnt+2000,:) = LSSn(Img6);
%%
%     [pano_BRISQUE(cnt,:), feature_BRISQUE(cnt,:)] = calcBRISQUE(Img1);
%     [pano_BRISQUE(cnt+400,:), feature_BRISQUE(cnt+400,:)] = calcBRISQUE(Img2);
%     [pano_BRISQUE(cnt+800,:), feature_BRISQUE(cnt+800,:)] = calcBRISQUE(Img3);
%     [pano_BRISQUE(cnt+1200,:), feature_BRISQUE(cnt+1200,:)] = calcBRISQUE(Img4);
%     [pano_BRISQUE(cnt+1600,:), feature_BRISQUE(cnt+1600,:)] = calcBRISQUE(Img5);
%     [pano_BRISQUE(cnt+2000,:), feature_BRISQUE(cnt+2000,:)] = calcBRISQUE(Img6);
%%
%      pano_HOSA(cnt,:) = calcHOSA(Img1);%y
%      pano_HOSA(cnt+400,:) = calcHOSA(Img2);
%      pano_HOSA(cnt+800,:) = calcHOSA(Img3);
%      pano_HOSA(cnt+1200,:) = calcHOSA(Img4);
%      pano_HOSA(cnt+1600,:) = calcHOSA(Img5);
%      pano_HOSA(cnt+2000,:) = calcHOSA(Img6);
%%
%      pano_NIQE(cnt,:) = calcNIQE(Img1);%y
%      pano_NIQE(cnt+400,:) = calcNIQE(Img2);
%      pano_NIQE(cnt+800,:) = calcNIQE(Img3);
%      pano_NIQE(cnt+1200,:) = calcNIQE(Img4);
%      pano_NIQE(cnt+1600,:) = calcNIQE(Img5);
%      pano_NIQE(cnt+2000,:) = calcNIQE(Img6);
%%
%      pano_QAC(cnt,:) = calcQAC(Img1);%y
%      pano_QAC(cnt+400,:) = calcQAC(Img2);
%      pano_QAC(cnt+800,:) = calcQAC(Img3);
%      pano_QAC(cnt+1200,:) = calcQAC(Img4);
%      pano_QAC(cnt+1600,:) = calcQAC(Img5);
%      pano_QAC(cnt+2000,:) = calcQAC(Img6);
%     pano_BPRI(cnt,:) = BPRI(img);%y
%    pano_BPRI_PSS(cnt,:) = PSS(img);%y
%     pano_BPRI_LSSs(cnt,:) = LSSs(img);%y
%     pano_BPRI_LSSn(cnt,:) = LSSn(img);%y
%     [pano_BRISQUE(cnt,:), feature_BRISQUE(cnt,:)] = calcBRISQUE(img);%y
%     pano_CORNIA = calcCORNIA(img);  %slow & occupy too much memory%y
%     pano_DipIQ = calcDipIQ(img);    %slow & occupy too much memory%y
%     pano_HOSA(cnt,:) = calcHOSA(img);%y
%     pano_ILNIQE(cnt,:) = calcILNIQE(img);%n
%     pano_LPSI(cnt,:) = LPSI(img);%n
%     pano_NIQE(cnt,:) = calcNIQE(img);%y
%     pano_QAC(cnt,:) = calcQAC(img);%y
    
    % -----------------------too slow--------------------------------------
    % pano_BLIINDS2 = calcBLIINDS2(img);  % slow
    % pano_DIVINE = calcDIVINE(img);    % slow
    % pano_NFERM = calcNFERM(img);  % slow
    
    % -------------------don't need compared-------------------------------
    % pano_ARISM = arismc_index(img);
    % pano_BIQI = biqi(img_gray);
    % pano_fisblim = fisblim_index(img);
    % pano_GMLF = Grad_LOG_CP_TIP(img);
    % pano_nfsdm = nfsdm_index(img);
    % pano_PSIM = ??
    % pano_SISBLIM1 = sisblim_sm_index(img);
    % pano_SISBLIM2 = sisblim_sfb_index(img);
    % pano_SISBLIM3 = sisblim_wm_index(img);
    % pano_SISBLIM4 = sisblim_wfb_index(img);
    % pano_VideoBLIINDS = ??
    % pano_VIIDEO = ??
end

