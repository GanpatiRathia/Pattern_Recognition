clc
clear
close all

I = imread('Lenna.png');
I1= rgb2gray(I);
figure(1);imshow(I1);
figure(2);imhist(I1);