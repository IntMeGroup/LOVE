function feat = BMPRI_feature(img)

JPEGfeat = LBPjpeg(img);
JP2Kfeat = LBPjp2k(img);
GBfeat = LBPgb(img);
WNfeat = LBPwn(img);

feat = [JPEGfeat JP2Kfeat GBfeat WNfeat];