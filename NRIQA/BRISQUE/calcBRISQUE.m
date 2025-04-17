function [score,feature] = calcBRISQUE(img)

CurrentPath = pwd;
[BrisquePath,~,~]=fileparts(which('calcBRISQUE'));
cd(BrisquePath)

%%
% Code from "function qualityscore  = brisquescore(imdist)"
if(size(img,3)==3)
    img = uint8(img);
    img = rgb2gray(img);
end
img = double(img);

if(nargin<2)
feature = brisque_feature(img);
disp('feat computed')
end


fid = fopen('test_ind','w');

for jj = 1:size(feature,1)
    
fprintf(fid,'1 ');
for kk = 1:size(feature,2)
fprintf(fid,'%d:%f ',kk,feature(jj,kk));
end
fprintf(fid,'\n');
end

fclose(fid);
warning off all
delete output test_ind_scaled dump
system('svm-scale -r allrange test_ind >> test_ind_scaled');
system('svm-predict -b 1 test_ind_scaled allmodel output >>dump');

load output
score = output;

%%
cd(CurrentPath)
