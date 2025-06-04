% ------------------------------------------------------------------------------------------
% Confusing image quality assessment: Towards better augmented reality experience
% Huiyu Duan, Xiongkuo Min, Yucheng Zhu, Guangtao Zhai, Xiaokang Yang, and Patrick Le Callet
% IEEE Transactions on Image Processing (TIP)
% ------------------------------------------------------------------------------------------

clc
close all
clear all
scores_original1=[];
scores_original2=[];
acceptIndex=[];
% path_database = '..\database1_cfiqa\';
% path_subjective_data = '..\database1_cfiqa\subjective_data\';
path_database = 'E:\AIGV60K\3050all\MOS\';
path_subjective_data = 'E:\AIGV60K\3050all\MOS\';
file_lists = dir(path_subjective_data);
subject_num = 0;
for cnt = 1:length(file_lists)
    if (length(file_lists(cnt).name) >3) && (strcmp(file_lists(cnt).name(end-3:end), '.csv') == 1)
        subject_num = subject_num+1;
        subject_num
        [numeric,text,raw] = xlsread([path_subjective_data,file_lists(cnt).name]);
        subject_data{subject_num} = numeric;
        temp_data = subject_data{subject_num};
        scores_original1(:,subject_num) = temp_data(:,1);
        scores_original2(:,subject_num) = temp_data(:,2);
        scores_original3(:,subject_num) = temp_data(:,3);
        scores_original4(:,subject_num) = temp_data(:,4);
        scores_original5(:,subject_num) = temp_data(:,5);
        scores_original6(:,subject_num) = temp_data(:,6);
        scores_original7(:,subject_num) = temp_data(:,7);
        scores_original8(:,subject_num) = temp_data(:,8);
        scores_original9(:,subject_num) = temp_data(:,9);
        scores_original10(:,subject_num) = temp_data(:,10);
        scores_original11(:,subject_num) = temp_data(:,11);
        scores_original12(:,subject_num) = temp_data(:,12);
        scores_original13(:,subject_num) = temp_data(:,13);
        scores_original14(:,subject_num) = temp_data(:,14);
        scores_original15(:,subject_num) = temp_data(:,15);
    


%% MOS
% ------------------compulate MOS with outliers removed--------------------
scoresOri = [scores_original1(:,subject_num), scores_original2(:,subject_num),scores_original3(:,subject_num),scores_original4(:,subject_num),scores_original5(:,subject_num), scores_original6(:,subject_num),scores_original7(:,subject_num),scores_original8(:,subject_num),scores_original9(:,subject_num), scores_original10(:,subject_num),scores_original11(:,subject_num),scores_original12(:,subject_num),scores_original13(:,subject_num), scores_original14(:,subject_num),scores_original15(:,subject_num)];
SCORE = ceil(scoresOri.*1);
% SCORE = scoresOri.*1;
scoreMeanImg = zeros(size(SCORE));
scoreStdImg = zeros(size(SCORE));
scoreMeanPerson = zeros(size(SCORE));
scoreStdPerson = zeros(size(SCORE));

% mean score for each image (another words: /(subjects' number)) (MOS)
for img = 1:size(SCORE,1)
    scoreMeanImg(img,:) = mean(SCORE(img,:));
    scoreStdImg(img,:) = std(SCORE(img,:));
end

% mean score for each subject (another words: /(images' number))
for person = 1:size(SCORE,2)
    scoreMeanPerson(:,person) = mean(SCORE(:,person));
    scoreStdPerson(:,person) = std(SCORE(:,person));
end

% remove outliers
reject = zeros(1,size(SCORE,2));
beta = kurtosis(SCORE')';
for person = 1:size(SCORE,2)
    P = 0;
    Q = 0;

    for img = 1:size(SCORE,1)

        if (beta(img)>=2)&&(beta(img)<=4)
            k = 2;
        else
            k = sqrt(20);
        end
        if SCORE(img,person) >= scoreMeanImg(img,person) + k*scoreStdImg(img,person)
            P = P+1;
        elseif SCORE(img,person) <= scoreMeanImg(img,person) - k*scoreStdImg(img,person)
            Q = Q+1;
        end
    end
    if ((P+Q)/size(SCORE,1)>0.05) && (abs((P-Q)/(P+Q))<0.3)
        reject(1,person) = 1;
    end
end
accept = ~reject;

for j = 1:size(SCORE,2)
    if accept(j)
        kk = ((beta>=2)&(beta<=4))*2 + ((beta<2)|(beta>4))*sqrt(20);
        acceptIndex(:,j) = (SCORE(:,j)>=(mean(SCORE,2)-kk.*std(SCORE,[],2))).*(SCORE(:,j)<=(mean(SCORE,2)+kk.*std(SCORE,[],2)));
    else
        acceptIndex(:,j) = 0;
    end
end

acceptIndex = logical(acceptIndex);
% for person = 1:size(SCORE,2)
%     for img = 1:size(SCORE,1)
%         mmax= max(scoresOri(img,:));
%         mmin= min(scoresOri(img,:));
%         id1=find(scoresOri(img,:)==mmax);
%         id2=find(scoresOri(img,:)==mmin);
%         acceptIndex(img,id1) = 0;
%         acceptIndex(img,id2) = 0;
%     end
% end
acceptSubjectIndex = acceptIndex(:,find(accept==1));
acceptRatio = 1-sum(sum(acceptSubjectIndex))/(size(acceptSubjectIndex,1)*size(acceptSubjectIndex,2));
for i = 1:size(SCORE,1)
    MOS(i,1) = mean(SCORE(i,acceptIndex(i,:)));
    SD(i,1) = std(SCORE(i,acceptIndex(i,:)));
    num_obs(i,1) = sum(acceptIndex(i,:));
end


SCOREz = (SCORE - scoreMeanPerson)./scoreStdPerson;
SCOREz = (SCOREz+3)*100/6;
for i = 1:size(SCOREz,1)
    MOSz(i,1) = mean(SCOREz(i,acceptIndex(i,:)));
end

%% Distribution of subjectibe quality scores in the database
% Distribution of subjectibe quality scores
numberTotal = zeros(1,5);
scoresAfterRemoveOutliers = SCORE.*acceptIndex;
for i = 1:subject_num
    for j = 1:5
        numberTotal(j) = numberTotal(j)+length(find(scoresAfterRemoveOutliers(:,i)==j));
    end
end
mymoz1(1,:,:) =  MOSz;
    end
end
% figure(1)
% colorbar=bar(numberTotal);
% grid on
% set(colorbar,'FaceColor',[0.5 0.4470 0.7410])
% axis([0 6 0 250]);
% xlabel('scores');
% ylabel('Image Number');
% title('Distribution of subjective Smoothness scores');

% % Distribution of lambda values
% figure(2)
% [numeric,text,raw] = xlsread([path_database,'thresholds.csv']);
% alpha_data = numeric;
% alpha(:,1) = alpha_data(:,3);
% alpha10 = ceil(alpha.*10);
% alpha_num = size(alpha10(:,1));
% numberTotal = zeros(1,10);
% for j = 1:10
%     numberTotal(j) = numberTotal(j)+length(find(alpha10(:,1)==j));
% end
% numberTotal(1) = (numberTotal(1)+numberTotal(10))/2;
% numberTotal(10) = (numberTotal(1)+numberTotal(10))/2;
% numberTotal(2) = (numberTotal(2)+numberTotal(9))/2;
% numberTotal(9) = (numberTotal(2)+numberTotal(9))/2;
% bar(numberTotal);
% axis([0 11 0 80]);
% xlabel('{\lambda}{\times}10');
% ylabel('Number');
% grid on
% title('Distribution of {\lambda} values');
% 
% % Distribution of subjective quality scores (0.3<{\lambda}<0.7)
% index1 = 0;
% index2 = 0;
% for i = 1:300
%     if (alpha(i,1)>0.3)&&(alpha(i,1)<0.7)
%         index1 = index1+1;
%         DistortionType(i,1) = 1;
%         DistortionType(i+300,1) = 1;
%     else
%         index2 = index2+1;
%         DistortionType(i,1) = 2;
%         DistortionType(i+300,1) = 2;
%     end
% end
% 
% DistortionIndex = [DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType DistortionType];
% numberTotal = zeros(1,10);
% scoresAfterRemoveOutliers = SCORE.*acceptIndex.*(DistortionIndex==1);
% for i = 1:subject_num
%     for j = 1:10
%         numberTotal(j) = numberTotal(j)+length(find(scoresAfterRemoveOutliers(:,i)==j));
%     end
% end
% figure(3)
% bar(numberTotal);
% axis([0 11 0 1600]);
% xlabel('scores');
% ylabel('Image Number');
% title('Distribution of subjective quality scores (0.3<{\lambda}<0.7)');
% 
% % Distribution of subjective quality scores (0.4<{\lambda}<0.6)
% index1 = 0;
% index2 = 0;
% for i = 1:300
%     if (alpha(i,1)>0.4)&&(alpha(i,1)<0.6)
%         index1 = index1+1;
%         DistortionType2(i,1) = 1;
%         DistortionType2(i+300,1) = 1;
%     else
%         index2 = index2+1;
%         DistortionType2(i,1) = 2;
%         DistortionType2(i+300,1) = 2;
%     end
% end
% 
% DistortionIndex2 = [DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2 DistortionType2];
% numberTotal = zeros(1,10);
% scoresAfterRemoveOutliers = SCORE.*acceptIndex.*(DistortionIndex2==1);
% for i = 1:subject_num
%     for j = 1:10
%         numberTotal(j) = numberTotal(j)+length(find(scoresAfterRemoveOutliers(:,i)==j));
%     end
% end
% figure(4)
% bar(numberTotal);
% axis([0 11 0 900]);
% xlabel('scores');
% ylabel('Image Number');
% title('Distribution of subjective quality scores (0.4<{\lambda}<0.6)');
% 
%% Distribution of MOSs
figure(5)
% C = colorplus([378 187 83]);
% C1 = C(1,:);
% C2 = C(2,:);
% C3 = C(3,:);
h1 = histogram(mymoz1(1,:,:))
% xlim([0 100])
% h = findobj(gca,'Type','patch');
% set(h,'facecolor',[0 0.4470 0.7410]);
set(h1,'facecolor',[0.48,0.71,0.85],'facealpha',0.8);
set(h1,'edgeColor','k');
grid on
xlabel('MOS');
ylabel('Image Number');
title('Distribution of MOSs');
h1.BinWidth = 5;
% figure(6)
% h4 = histfit(MOSz);
% set(h4,'Color','k');
% 
% hold on
% h2 = histogram(MOSz(find(DistortionType==1)))
% hold on
% h3 = histogram(MOSz(find(DistortionType2==1)))
% h1.Normalization = 'count';
% h1.BinWidth = 5;
% h2.Normalization = 'count';
% h2.BinWidth = 5;
% h3.Normalization = 'count';
% h3.BinWidth = 5;
% 
% % complete the axis value
% y1 = [1 4 15 31 40 49 79 79 80 75 48 50 29 15 3 2 0];
% x1 = [10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90];
% % y2 = [5 15 27 39 72 75 80 71 45 32 8 1 0];
% % x2 = [20 25 30 35 40 45 50 55 60 65 70 75 80];
% % y3 = [1 8 11 17 45 49 57 38 24 9 3 0];
% % x3 = [20 25 30 35 40 45 50 55 60 65 70 75];
% y2 = [0 0 5 15 27 39 72 75 80 71 45 32 8 1 0 0 0];
% x2 = [10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90];
% y3 = [0 0 1 8 11 17 45 49 57 38 24 9 3 0 0 0 0];
% x3 = [10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90];
% x = 0:0.1:100;
% f = fit(x1'+2.5,y1','gauss1')
% y = f(x);
% hold on
% plot(x,y,'LineWidth',1.5)
% f = fit(x2'+2.5,y2','gauss1')
% y = f(x);
% hold on
% plot(x,y,'LineWidth',1.5)
% f = fit(x3'+2.5,y3','gauss1')
% y = f(x);
% hold on
% plot(x,y,'LineWidth',1.5)
% legend('Entire database','0.3<{\lambda}<0.7','0.4<{\lambda}<0.6','Gaussian fitting ({\sigma}=21.07)','Gaussian fitting ({\sigma}=16.36)','Gaussian fitting ({\sigma}=13.24)')
% grid on