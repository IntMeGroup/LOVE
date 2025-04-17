
============================================================================================
The blind pseudo reference image based (BPRI) quality measure
Copyright(c) 2018 Xiongkuo Min, Ke Gu, Guangtao Zhai, Jing Liu, Xiaokang Yang, and Chang Wen Chen
All Rights Reserved.

--------------------------------------------------------------------------------------------
Permission to use, copy, or modify this software and its documentation for educational
and research purposes only and without fee is hereby granted, provided that this copyright
notice and the original authors' names appear on all copies and supporting documentation.
This software shall not be used, redistributed, or adapted as the basis of a commercial
software or hardware product without first obtaining permission of the authors. The authors
make no representations about the suitability of this software for any purpose. It is
provided "as is" without express or implied warranty.
--------------------------------------------------------------------------------------------

This is the blind pseudo reference image based (BPRI) measure described in the following paper:

Xiongkuo Min, Ke Gu, Guangtao Zhai, Jing Liu, and Xiaokang Yang, "Blind Quality Assessment 
Based on Pseudo Reference Image," IEEE Transactions on Multimedia, 2018.

Please contact Xiongkuo Min (minxiongkuo@gmail.com) if you have any questions.

--------------------------------------------------------------------------------------------

Demo code:
demo.m

The BPRI quality measure:
function [BPRIp,BPRIc] = BPRI(img)
Input:  (1) img: test image
Output: (1) BPRIp: the quality score computed by the probability weighting strategy (default)
        (2) BPRIc: the quality score computed by the hard classification strategy
Usage:  Given a test image img, whose dynamic range is 0-255
        [BPRIp,BPRIc] = BPRI(img);

The PSS blockiness measure:
function score = PSS(img)
Input : (1) img: test image
Output: (1) score: the blockiness score
Usage:  Given a test image img, whose dynamic range is 0-255
        score = PSS(img);

The LSSs sharpness measure:
function score = LSSs(img)
Input : (1) img: test image
Output: (1) score: the sharpness score
Usage:  Given a test image img, whose dynamic range is 0-255
        score = LSSs(img);

The LSSn noiseness measure:
function score = LSSn(img)
Input : (1) img: test image
Output: (1) score: the noiseness score
Usage:  Given a test image img, whose dynamic range is 0-255
        score = LSSn(img);

============================================================================================
