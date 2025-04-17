function patches= compute_patches(M, block_size,step)

M = M(3:end-2,3:end-2);
[r,c]= size(M);
if ~exist('step','var')
    step = round(max(r,c)/400*block_size);
end
[xc,yc] = meshgrid(0:step:c,0:step:r);
rm_ind = ((xc+block_size)>c)|((yc+block_size)>r);
xc(rm_ind) = [];
yc(rm_ind) = [];
pathch_num = numel(xc);
patches = zeros(pathch_num,block_size*block_size);
for i = 1:block_size
    for j = 1:block_size
        ind = sub2ind(size(M),yc+i,xc+j);
%         disp([i,j,size(patches),nnz(ind)])
        patches(:,(i-1)*block_size+j) = M(ind(:));
    end
end
patches = patches';