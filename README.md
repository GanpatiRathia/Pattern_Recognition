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
        
Given three points, determine the one which is closest to the given observations: X1=30 20 133 189.6
X2=22 30 100.06 126.0075
X3=28.47 20.11 133.06 188.90


    
 
