
clear;
clc;

% Read the image
img = imread('img.png');

% Compute the overall quality (two strategies)
[BPRIp,BPRIc] = BPRI(img);

% Compute the overall quality (one strategy)
BPRIs = BPRI(img);

% Compute the blockiness score
blockiness = PSS(img);

% Compute the sharpness score
sharpness = LSSs(img);

% Compute the noiseness score
noiseness = LSSn(img);
