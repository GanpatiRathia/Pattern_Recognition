clear all
close all
clc 

jp = dir('*.jpg');
nm = length(jp);
md = cell(1,nm);
for k = 1 : nm
    md{k}= rgb2gray(imread(jp(k).name));
end

% imshow(md{3})

for i = 1 : 24 
    g{i} = graycomatrix(md{i}) ;
    h{i} = graycoprops(g{i}) ;
end

h = h';
a2 = cell2mat(h) ;
a = a2 
a = (cell2mat(struct2cell(a)))' ;

a1 = sortrows(a','ascend') ;
a1 = (a1)';
a1 = a1(:,1:3) ;

scatter3(a1(:,1),a1(:,2),a(:,3)) ;

b = [ 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0] ;
model = fitcnb(a1,b) ;


%{
x1range = min(a1(:,1):.0.01:max(a1(:,1)) ;
x2range = min(a1(:,2):.0.01:max(a1(:,2)) ;
x3range = min(a1(:,3):.0.01:max(a1(:,3)) ;
[xx1, xx2, xx3] = meshgrid(x1range,x2range,x3range) ;
xgrid = [xx1(:) xx2(:) xx3(:)] ;

for j = 1 : numel(model) 
   ps = predict {model{i},xgrid) ;
   subplot(2,2,i) ;
   gscatter(xx1(:),xx2

%}
classifier = 'nbc';
cp = classifierTrain(classifier,a1) ;
figure ;
classifierPlot(classifier,a1,cp,'decBoundary') ;