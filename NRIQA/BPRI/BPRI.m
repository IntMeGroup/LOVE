function [BPRIp,BPRIc] = BPRI(img)
% Input:  (1) img: test image
% Output: (1) BPRIp: the quality score computed by the probability weighting strategy (default)
%         (2) BPRIc: the quality score computed by the hard classification strategy
% Usage:  Given a test image img, whose dynamic range is 0-255
%         [BPRIp,BPRIc] = BPRI(img);

Feature(1) = LSSs(img);
Feature(2) = LSSn(img);
Feature(3) = PSS(img);

load para.mat
FeatureMapped(1) = align(paraLSSs,Feature(1));
FeatureMapped(2) = align(paraLSSn,Feature(2));
FeatureMapped(3) = align(paraPSS,Feature(3));

[Type,Pro] = classifyType(Feature);

BPRIp = sum(FeatureMapped.*Pro);
BPRIc = FeatureMapped(Type);

end