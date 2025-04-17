function score = PSS(img)
% Input : (1) img: test image
% Output: (1) score: the blockiness score
% Usage:  Given a test image img, whose dynamic range is 0-255
%         score = PSS(img);
if size(img,3)==3
    img = rgb2gray(img);
end

cc = corner(img,'MinimumEigenvalue',1000000,'FilterCoefficients',fspecial('gaussian',[3 1],0.5),'QualityLevel',0.001);
pp=cc(((mod(cc(:,1),8)==1)|(mod(cc(:,1),8)==0))&((mod(cc(:,2),8)==1)|(mod(cc(:,2),8)==0)),:);

fileName = [num2str(randi(intmax)) '.jpg'];
imwrite(img,fileName,'quality',0);
imgPRI = imread(fileName);
delete(fileName);
ccPRI = corner(imgPRI,'MinimumEigenvalue',1000000,'FilterCoefficients',fspecial('gaussian',[3 1],0.5),'QualityLevel',0.001);
ppPRI = ccPRI(((mod(ccPRI(:,1),8)==1)|(mod(ccPRI(:,1),8)==0))&((mod(ccPRI(:,2),8)==1)|(mod(ccPRI(:,2),8)==0)),:);

overlap = intersect(pp,ppPRI,'rows');
score = length(overlap)/(length(ppPRI)+1);

end