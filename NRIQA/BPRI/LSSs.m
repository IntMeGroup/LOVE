function score = LSSs(img)
% Input : (1) img: test image
% Output: (1) score: the sharpness score
% Usage:  Given a test image img, whose dynamic range is 0-255
%         score = LSSs(img);
if size(img,3)==3
    img = rgb2gray(img);
end
img = uint8(img);

% PRI deriving
win = ones(3)/9;
imgPRI = imfilter(img,win);

mapDIST = LBP41(img);
mapPRI = LBP41(imgPRI);

score = sum(sum(mapDIST.*mapPRI))/(sum(sum(mapPRI|mapDIST))+1);

end

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function lbp_map = LBP41(img)
% Calculate the LBP statistics using a neighbors number of 4 and a radius of 1
img = double(img);
img = mat2gray(img);

neighborNum = 4;
[M,N] = size(img);
% Coordinate offset of neighbors
offset = [0 1; -1 0; 0 -1; 1 0];
% Block size
bsize_M = 3;
bsize_N = 3;
% Starting coordinate
orig_m = 2;
orig_n = 2;
% d_m and d_n
d_m = M - bsize_M;
d_n = N - bsize_N;

% Center pixel matrix
Center = img(orig_m:orig_m+d_m,orig_n:orig_n+d_n);
% LBP matrix
LBP = zeros(d_m+1,d_n+1);

% Compute the LBP code matrix
D = cell(neighborNum,1);
for i = 1:neighborNum
    m = offset(i,1) + orig_m;
    n = offset(i,2) + orig_n;
    Neighbor = img(m:m+d_m,n:n+d_n);
    D{i} = Neighbor >= Center;
end

% Accumulate all neighbors
for i = 1:neighborNum
	LBP = LBP + D{i};
end

lbp_map = (LBP == 2) | (LBP == 3);

end