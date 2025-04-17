function [fv] = hosa_feature_extraction (centroid, variance, skewness, M, P, BS, power, img)

if size(img,3)~=1,
    img = double(rgb2gray(img));
else
    img = double(img);
end

% regular grid
[row, col] = size(img);
step = floor(sqrt(row*col/10000)); 
if step<1,
    step = 1;
end
patches = compute_patches(img, BS, step);

% patch normalization
patches = bsxfun(@rdivide, bsxfun(@minus, patches, mean(patches)), sqrt(var(patches)+10));
patches = bsxfun(@minus, patches', M) * P; 
patches = patches';


n = size (patches, 2);  % number of local fetures
d = size (patches, 1);  % feature dimensionality
k = size (centroid, 2);  % number of codewords

% distance
patches = patches';
distMx = repmat(sum(centroid.^2),n,1)-patches*centroid*2+repmat(sum(patches.^2, 2),1,k); 

gamma = 0.05; % gaussian kernel
r = 5; % 5 nearest codewords
mean_diff = zeros (d, k);
var_diff = zeros(d, k);
skn_diff = zeros(d, k);
[d_sorted, pos] = sort(distMx, 2);

% Gaussian kernel similarity
weights = exp(-gamma*d_sorted(:, 1:r))./repmat(sum(exp(-gamma*d_sorted(:, 1:r))')', 1, r);
  
for i = 1:k,
    idx = [];
    weights_temp = [];
    for j = 1:r
        pos_temp = pos(:, j);
        idx_temp = find(pos_temp == i);
        idx = [idx; idx_temp];
        weights_temp = [weights_temp; weights(idx_temp, j)];
    end
    
    if ~isempty(weights_temp)
        weights_temp = weights_temp./sum(weights_temp); % weight normalization
        
        if length(idx) == 1
            mean_diff (:, i) = mean_diff(:, i) + (repmat(weights(idx, j), 1, d).* (patches(idx, :)  - repmat(centroid (:, i)', length(idx), 1)))';
        
        elseif length(idx) >1
            weighted_mean = sum(repmat(weights_temp, 1, d).* patches(idx, :))';
            mean_diff (:, i) = mean_diff(:, i) + weighted_mean  - centroid (:, i);
            
            if  sum(var(patches(idx, :)))>1e-8
                var_diff(:, i) = var(patches(idx, :), weights_temp)' - variance(:, i);
                skn_diff(:, i) = (sum(repmat(weights_temp, 1, d).* (patches(idx, :) - repmat(weighted_mean', length(idx), 1)).^3)') ./ ...
                    (var(patches(idx, :), weights_temp)' .^(3/2)+1e-4) - skewness(:, i);
            end
        end
    end
end

mean_diff = reshape (mean_diff, k*d, 1);
var_diff = reshape (var_diff, k*d, 1);
skn_diff = reshape (skn_diff, k*d, 1);
fv = [mean_diff; var_diff; skn_diff];

% feature normalizaiton
fv = sign(fv) .* (abs(fv).^power);
fv = bsxfun(@rdivide, fv, sqrt(sum(fv.^2)) + 1e-20);

end