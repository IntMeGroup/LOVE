function [Type,Pro] = classifyType(Feature)

CurrentPath = pwd;
[SVMpath,~,~]=fileparts(which('classifyType'));
cd([SVMpath '\SVM'])

fid = fopen('test_ind.txt','w');
for itr_im = 1:size(Feature,1)
    fprintf(fid,'%d ',1);
    for itr_param = 1:size(Feature,2)
        fprintf(fid,'%d:%f ',itr_param,Feature(itr_im,itr_param));
    end
    fprintf(fid,'\n');
end
fclose(fid);
delete test_ind_scaled
system('svm-scale -l 0 -u 1 -r range test_ind.txt >> test_ind_scaled');
system('svm-predict -b 1 test_ind_scaled model output.txt>dump');

output = textread('output.txt','%s');
Type = str2double(output{5,1});
Pro = [str2double(output{6,1}) str2double(output{7,1}) str2double(output{8,1})];

cd(CurrentPath)