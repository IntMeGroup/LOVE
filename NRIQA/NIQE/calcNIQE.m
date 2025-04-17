function score = calcNIQE(img)
% Input
% img              - Image whose quality needs to be computed
% min size: 96x96

CurrentPath = pwd;
[NiqePath,~,~]=fileparts(which('calcNIQE'));
cd(NiqePath)

load modelparameters.mat;
blocksizerow = 96;
blocksizecol = 96;
blockrowoverlap = 0;
blockcoloverlap = 0;
score = computequality(img,blocksizerow,blocksizecol,blockrowoverlap,blockcoloverlap,mu_prisparam,cov_prisparam);

cd(CurrentPath)
