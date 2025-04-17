function [score,fv] = calcHOSA(img)

CurrentPath = pwd;
[HosaPath,~,~]=fileparts(which('calcHOSA'));
cd(HosaPath)

load('whitening_param.mat', 'M', 'P');
load('codebook_hosa', 'codebook_hosa');
BS = 7; % patch size
power = 0.2; % signed power normalizaiton param

% feature extraction
fv = hosa_feature_extraction(codebook_hosa.centroid_cb, codebook_hosa.variance_cb, ...
    codebook_hosa.skewness_cb, M, P, BS, power, img);

% quality prediction
fv = sparse(fv);
load('hosa_live_model');
score = liblinearpredict(1, fv', hosa_live_model);

cd(CurrentPath)