
clear;
clc;

% Read the image
img = imread('img.png');

% Compute the quality
score = BMPRI(img)
