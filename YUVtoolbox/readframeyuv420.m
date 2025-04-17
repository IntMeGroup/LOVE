function [y, cb, cr] = readframeyuv420(fileID,height,width)
y = fread(fileID,width*height, 'uchar')';
cb = fread(fileID,width*height/4, 'uchar')';
cr = fread(fileID,width*height/4, 'uchar')';