function Q = QAC(im,cluster_center,feature_fun,blksize,step)

if ~exist('step','var')
    step = 12;
end
if ~exist('blksize','var')
    blksize = sqrt(size(cluster_center{1}.centroids,2)/3);
end
double_image = double((im))/255;
feature_pixel_arrary = (feature_fun(double_image,blksize,step)); % feature computation
feature_pixel_arrary = abs(feature_pixel_arrary);

feature_pixel_arrary = feature_pixel_arrary';
num_patches = size(feature_pixel_arrary,1);

K = size(cluster_center{1}.centroids,1); % the number of clusters at each quality level
num_levels = length(cluster_center); % the number of the quality levels
dist_mat = zeros(num_patches,K*num_levels); % distance compuatation between the features in im and the cluster centers
dist_mat_level = zeros(num_patches,num_levels); % Only the nearest center at each level  is preserved  for every feature.
ind_level = zeros(num_patches,num_levels);% the quality level of the ordered cluster centers for each feature.


for i= 1:num_levels
    dist_mat(:,((i-1)*K+1):(i*K)) = EuDist2(feature_pixel_arrary, cluster_center{i}.centroids/255,1);
    dist_mat(:,((i-1)*K+1):(i*K)) = dist_mat(:,((i-1)*K+1):(i*K));
    [dist_mat_level(:,i) ind_level(:,i)] = min(dist_mat(:,((i-1)*K+1):(i*K)),[],2);
    ind_level(:,i) = ind_level(:,i) +(i-1)*K;
end

[dis_sort, indL] = 	sort(dist_mat_level,2,'ascend');
Q = [];
dis_minL = dis_sort;
Q_mat = ceil(indL/1)/num_levels;

weight  = exp(-(dis_minL)/32)+eps;

L = 2;%the used levels can vary from 1 to L. On the LIVE database, we set L to 2.
weight_mat = weight(:,1:L);
weight_mat = bsxfun(@times,weight_mat,1./sum(weight_mat,2));
Qm = Q_mat(:,1:L);
QL = Qm.*weight_mat;
Q = [Q, mean(sum(QL,2))];

