function score = BMPRI_score(feat)

CurrentPath = pwd;
[SVMpath,~,~]=fileparts(which('BMPRI_score'));
cd([SVMpath '\SVM'])

fid = fopen('test_ind.txt','w');
for itr_im = 1:size(feat,1)
    fprintf(fid,'%d ',1);
    for itr_param = 1:size(feat,2)
        fprintf(fid,'%d:%f ',itr_param,feat(itr_im,itr_param));
    end
    fprintf(fid,'\n');
end
fclose(fid);
delete test_ind_scaled
system('svm-scale -r range test_ind.txt >> test_ind_scaled');
system('svm-predict  -b 1  test_ind_scaled model output.txt>dump');
load output.txt;
score = output;

cd(CurrentPath)