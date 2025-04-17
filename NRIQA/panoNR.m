% -------------------------------------------------------------------------
% calculate NR-IQA of panoramic images
% -------------------------------------------------------------------------
%clear all

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
ImgPath = 'F:\allimg\img\';
ImgNumber = 2400;
% distortion
for i = 1:ImgNumber
    % if mod(i-1,20)<5
       ImgName{i,1} = [num2str(i-1),'.png'];
    % else
    %     ImgName{i,1} = [num2str(i),'.bmp'];
    % end
end

%% Calculate all NR-IQA algorithms
for cnt = 1:ImgNumber
    cnt
    
    Img = imread([ImgPath ImgName{cnt,1}]);
    img = Img;
    img_gray = rgb2gray(Img);
    
%     pano_BMPRI(cnt,:) = BMPRI(img);
%     pano_BPRI(cnt,:) = BPRI(img);
%     pano_BPRI_PSS(cnt,:) = PSS(img);
%     pano_BPRI_LSSs(cnt,:) = LSSs(img);
%     pano_BPRI_LSSn(cnt,:) = LSSn(img);
    [pano_BRISQUE(cnt,:), feature_BRISQUE(cnt,:)] = calcBRISQUE(img);
%     pano_CORNIA = calcCORNIA(img);  %slow & occupy too much memory
%     pano_DipIQ = calcDipIQ(img);    %slow & occupy too much memory
%     pano_HOSA(cnt,:) = calcHOSA(img);
%     pano_ILNIQE(cnt,:) = calcILNIQE(img);
%     pano_LPSI(cnt,:) = LPSI(img);
%     pano_NIQE(cnt,:) = calcNIQE(img);
%     pano_QAC(cnt,:) = calcQAC(img);
    
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

