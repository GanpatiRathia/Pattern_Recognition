import numpy as np
import math

# INPUT MATRIX
m = 14
n = 4
matrix = [[28.0, 31.0, 130.0, 68.12], [24.0, 28.0, 143.0, 127.89], [28.0, 20.0, 136.0, 89.03], [32.0, 34.0, 130.5, 78.28], [22.0, 15.0, 125.0, 134.08], [26.0, 37.0, 147.5, 135.31], [24.0, 19.0, 135.0, 130.48], [28.0, 22.0, 125.0, 86.48], [24.0, 26.0, 127.0, 129.47], [30.0, 21.0, 139.0, 82.43], [22.0, 20.0, 121.5, 127.41], [30.0, 38.0, 150.5, 71.21], [24.0, 17.0, 120.0, 132.06], [26.0, 20.0, 125.0, 90.85]]
# Vector1
vector1 = np.zeros((1,n))
vector1[0][0] = 30
vector1[0][1] = 20
vector1[0][2] = 133
vector1[0][3] = 189.6
# Vector2
vector2 = np.zeros((1,n))
vector2[0][0] = 22
vector2[0][1] = 30
vector2[0][2] = 100.06
vector2[0][3] = 126.0075
# Vector3
vector3 = np.zeros((1,n))
vector3[0][0] = 28.47
vector3[0][1] = 20.11
vector3[0][2] = 133.06
vector3[0][3] = 188.90                    
print("\n\nInput observations :\n{}".format(matrix))

#1 Compute mean
mean_input = np.zeros((1,n))
for i in range(0,n):
    mean_input[0][i] = (np.mean([row[i] for row in matrix]))
print("\n\nMean :{}".format(mean_input))

#2 Subtract mean from the data
for row in matrix:
    for j in range(0,n):
        row[j]=row[j]-mean_input[0][j]      

#3 Compute Covariance amtrix
matrix_transpose = np.transpose(matrix)
intermediate_matrix = np.matmul(matrix_transpose,matrix)
covariance_matrix = (1/(m-1)) * intermediate_matrix
print("\n\nCovariance matrix :\n{}".format(covariance_matrix))

#4 Finding inverse of covariance matrix
determinant = np.linalg.det(covariance_matrix)
inverse_matrix = np.linalg.inv(covariance_matrix)

#5 computing (Hq - Ht)
'''v1,v2,v3 are the 3 vectors
   im1,im2,im3,im4 are intermediate matrices'''
v1_im1 = mean_input - vector1
v2_im1 = mean_input - vector2
v3_im1 = mean_input - vector3

#6 Computing mahalonabis distance,Dm = (Hq - Ht)T * inverse_matrix * (Hq - Ht)
v1_im2 = np.transpose(v1_im1)
v2_im2 = np.transpose(v2_im1)
v3_im2 = np.transpose(v3_im1)

v1_im3 = np.matmul(v1_im1,inverse_matrix)
v2_im3 = np.matmul(v2_im1,inverse_matrix)
v3_im3 = np.matmul(v3_im1,inverse_matrix)

v1_im4 = np.matmul(v1_im3,v1_im2)
v2_im4 = np.matmul(v2_im3,v2_im2)
v3_im4 = np.matmul(v3_im3,v3_im2)

d1 = math.sqrt(v1_im4)
d2 = math.sqrt(v2_im4)
d3 = math.sqrt(v3_im4)
print("\n\nMahalanobis distances for \n{} is {},\n{} is {},\n{} is {}.".format(vector1,d1,vector2,d2,vector3,d3))
lt = []
lt.append(d1)
lt.append(d2)
lt.append(d3)
print("\n\nMinimum distance is {}".format(min(lt)))
print("\nVector{} is closest to the given Input observations.".format((np.argmin(lt))+1))
