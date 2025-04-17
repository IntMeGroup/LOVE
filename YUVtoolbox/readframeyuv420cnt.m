function [y, cb, cr] = readframeyuv420cnt(fileID,height,width,framenum)
fseek(fileID,(framenum-1)*width*height*1.5,'bof');
y = fread(fileID,width*height, 'uchar')';
cb = fread(fileID,width*height/4, 'uchar')';
cr = fread(fileID,width*height/4, 'uchar')';