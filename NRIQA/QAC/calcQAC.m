function score = calcQAC(img)

CurrentPath = pwd;
[TargetPath,~,~]=fileparts(which('calcQAC'));
cd(TargetPath)

load cluster_center;
if size(img,3)==3
    img = rgb2gray(img);
end
feature_fun = @compute_DOG;
score = QAC(img, cluster_center, feature_fun);

cd(CurrentPath)
