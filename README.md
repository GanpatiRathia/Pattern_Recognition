# Pattern_Recognition

## 1. Load grayscale lena image, plot its histogram.
```python
lena512= imread('lena512.bmp');
histogram(lena512);
title('Histogram of lena image');
xlabel('Gray Level');
ylabel('Pixel Count');
```

## 2.Write a program to compute Mahalanobis distance for the following 14 observations (It can be verified with the example solved in class) each of which is a 4-d vector.

| V1=28 | 31 | 130.0 |68.12|
|------|---|------|-----|
| V2=24 | 28 |143.0 |127.89| 
| V3=28 |20 |136.0 |89.03|
| V4=32 |34 |130.5 |78.28|
| V5=22 |15 |125.0 |134.08|
| V6=26 |37 |147.5 |135.31|
| V7=24 |19 |135.0 |130.48|
| V8=28 |22 |125.0 |86.48|
| V9=24 |26 |127.0 |129.47|
| V10=30 |21 |139.0 |82.43|
| V11=22 |20 |121.5 |127.41|
| V12=30 |38 |150.5 |71.21|
| V13=24 |17 |120.0 |132.06|
| V14=26 |20 |125.0 |90.85|
        
Given three points, determine the one which is closest to the given observations: 
X1=30 20 133 189.6<br>
X2=22 30 100.06 126.0075<br>
X3=28.47 20.11 133.06 188.90<br>
Display the intermediate results (mean and covariance matrix).

```python
V=[ 28, 31, 130, 68.12;
    24, 28, 143, 127.89;
    28, 20, 136, 89.03;
    32, 34, 130.5, 78.28;
    22, 15, 125, 134.08;
    26, 37, 147.5 135.31;
    24, 19, 135, 130.48;
    28, 22, 125, 86.48;
    24, 26, 127, 129.47;
    30, 21, 139, 82.43;
    22, 20, 121.5, 127.41;
    30, 38, 150.5, 71.21;
    24, 17, 120, 132.06;
    26, 20, 125, 90.85];

X=[30,20,133,189.6;
    22,30,100.6,126.0075;
    28.47,20.11,133.06,188.90];


D=zeros(3,1);
Vmean=mean(V,1)
Vcov=cov(V)
VcovI=inv(Vcov)
(X(1,:)-Vmean)
(X(2,:)-Vmean)
(X(3,:)-Vmean)


for i=1:3
    D(i)=sqrt((X(i,:)-Vmean)*VcovI*((X(i,:)-Vmean)'));
end

D
[M,I]=min(D);

fprintf("\nThe closest point is X%d with distance %f\n",I,M);
```
## 3.Given the following 3-d vectors:
P= [70,90,80] <br> Q= [40,6,6] <br> R= [10,20,30] <br> S= [32,43,55] <br> T= [70,60,40]<br>
Compute the Euclidean distance and highlight the point which is closer to the vector X= [25,20,40] and obtain the 3-d plot for the same.

```python
P=[70,90,80];
Q=[40,6,6];
R=[10,20,30];
S=[32,43,55];
T=[70,60,40];

X=[25,20,40];

a = ['P','Q','R','S','T','X']';
b = num2str(a);
c =cellstr(b);

D=zeros(5,1);
D(1)=sqrt(sum((X-P).^2));
D(2)=sqrt(sum((X-Q).^2));
D(3)=sqrt(sum((X-R).^2));
D(4)=sqrt(sum((X-S).^2));
D(5)=sqrt(sum((X-T).^2));
[value,index]=min(D);

if index==1
    fprintf("P is the closest\n");
elseif index==2
    fprintf("Q is the closest ");
elseif index==3
    fprintf("R is the closest ");
elseif index==2
    fprintf("S is the closest ");
else
    fprintf("T is the closest ");
end
fprintf("with distance %f\n",value);
x=[70,40,10,32,70,25];
y=[90,6,20,43,6,20];
z=[80,6,30,55,40,40];

point_id=[P,Q,R,S,T,X];
scatter3(x,y,z,'b*')
hold on
scatter3(x(6),y(6),z(6),'g*') %given vector
scatter3(x(index),y(index),z(index),'r*') %min distance vector
hold off
text(x,y,z,c,'Fontsize',12)
```

## 4.Compare two text files doc1.txt and doc2.txt using cosine distance. doc1.txt
MATLAB is a program for solving engineering and mathematical problems. The basic MATLAB objects are vectors and matrices, so you must be familiar with these before making extensive use of this program.
doc2.txt
MATLAB works with essentially one kind of object, a rectangular numerical matrix. Here is some basic information on using MATLAB matrix commands.

```python
str1=fileread('doc1.txt');
c1=strsplit(str1, {' ',',','.','\n'});
str2=fileread('doc2.txt');
c2=strsplit(str2, {' ',',','.','\n'});
dic=union(c1,c2);

finalList=dic(2:size(dic,2));
finalList
vectorOne=zeros(size(finalList,2),1);
vectorTwo=zeros(size(finalList,2),1);

for i=1:size(c1,2)
    pos=find(strcmp(finalList,c1(i)));
    vectorOne(pos,:)=vectorOne(pos,:)+1;
end

for i=1:size(c2,2)
    pos=find(strcmp(finalList,c2(i)));
    vectorTwo(pos,:)=vectorTwo(pos,:)+1;
end

%find cosine distance
similarity=(sum(vectorOne.*vectorTwo))/(sqrt(sum(vectorOne.^2))*sqrt(sum(vectorTwo.^2)))
distance=1-similarity
```
