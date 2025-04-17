function feat = LBPjpeg(img)
% Input : (1) img: a RGB or gray scale image, and the dynamic range should be 0-255.
% Output: (1) score: the quality score
if size(img,3)==3
    img_gray = rgb2gray(img);
else
    img_gray = img;
end
img_gray = uint8(img_gray);
mapDIST = LBP41(img_gray);

Q = [0 2 4 6 8];
for i = 1:length(Q)
    tmpName = [num2str(randi(intmax)) '.jpg'];
    imwrite(img,tmpName,'quality',Q(i));
    imgPRI = imread(tmpName);
    delete(tmpName);
    
    if size(imgPRI,3)==3
        imgPRI = rgb2gray(imgPRI);
    end
    imgPRI = uint8(imgPRI);
    mapPRI = LBP41(imgPRI);
    
    feat(1,i) = sum(sum(mapPRI.*mapDIST))/(sum(sum(mapPRI))+1);
end

end

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function lbp_map = LBP41(img)
% Calculate the LBP statistics using a neighbors number of 4 and a radius of 1
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

lbp_map = (LBP == 0) ; 

end

