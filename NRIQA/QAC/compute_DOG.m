function [dog_pixel_arrary ]= compute_DOG(double_image,blksize,step)

% sigmas = [0.5,1,2,4,8,16];
% sigmas = [0.5,1,2,4,8,16];
% double_image  = imdowmsample(double_image);
sigmas = [0.5, 2,4, ];
numscales = 3;
dog_pixel_arrary = [];

%     if ~exist('step','var')
%     dog_pixel_arrary = [dog_pixel_arrary;compute_patches(double_image,blksize)];%setp
%     else
%         dog_pixel_arrary = [dog_pixel_arrary;compute_patches(double_image,blksize,step)];
%     end
% k = [1,4,8];
% dog_hist = [];

for i = 1:numscales
    sigma = sigmas(i);
    hsize = 2*ceil(3*sigma)+1;
    gau = fspecial('gaussian',hsize,sigma);
    gau = gau/sum(gau(:));
    gau_image = imfilter(double_image, gau, 'symmetric','same');
    dog_map = (double_image-gau_image)*(4/sigma);
    if ~exist('step','var')
    dog_pixel_arrary = [dog_pixel_arrary;compute_patches(dog_map,blksize)];%setp
    else
        dog_pixel_arrary = [dog_pixel_arrary;compute_patches(dog_map,blksize,step)];
    end
%     double_image = gau_image;
    
end


