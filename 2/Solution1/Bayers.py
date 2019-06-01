"""
Engineer : Nitesh
Date : 7/03/19
Title : PR_Assignment_2_BayersClassifier

"""


import numpy as np
import operator
import pandas as pd
from scipy.spatial import distance
import math
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt 

def Bayers():
    iris = load_iris()
    x = iris.data
    y = iris.target
    setosa_val = x[0:50]
    setosa_label = y[0:50]
    versicolor_val , versicolor_label = x[50:100] , y[50:100]
    verginica_val , verginica_label = x[100:150] ,y[100:150]
    # print(len(x1))
    # print(x2)
    setosa_train,setosa_test = train_test_split(setosa_val,test_size=0.2)
    versicolor_train,versicolor_test = train_test_split(versicolor_val,test_size=0.2)
    verginica_train,verginica_test = train_test_split(verginica_val,test_size=0.2)

    
    xMean1 = np.mean(setosa_train,axis=0)
    xMean2 = np.mean(versicolor_train,axis=0)
    xMean3 = np.mean(verginica_train,axis=0)
    
    print("Mean of the C1 = ",xMean1)
    print("Mean of the C2 = ",xMean2)
    print("Mean of the C3 = ",xMean3)

    covX1 = np.cov(setosa_train,rowvar=False)
    covX2 = np.cov(versicolor_train,rowvar=False)
    covX3 = np.cov(verginica_train,rowvar=False)

    invCov1 = np.linalg.inv(covX1)
    invCov2 = np.linalg.inv(covX2)
    invCov3 = np.linalg.inv(covX3)

    det1 = np.linalg.det(invCov1)
    det2 = np.linalg.det(invCov2)
    det3 = np.linalg.det(invCov3)

    print("Coveriance Matrice C1= \n",covX1)
    print("Inverse Of Cov C1= \n",invCov1)
    print("Det of inv of C1 ",det1)

    print("Coveriance Matrice C2= \n",covX2)
    print("Inverse Of Cov C2= \n",invCov2)
    print("Det of inv of C2 ",det2)

    print("Coveriance Matrice C3= \n",covX3)
    print("Inverse Of Cov C3= \n",invCov3)
    print("Det of inv of C3 ",det3)

    # power1 = math.pow(distance.mahalanobis(x1,xMean1,invCov1),2)
    # print(power1)
    ans_setosa_test = []
    # result_setosa = []
    ans_versicolor_test = []
    # result_versicolor = []
    ans_verginica_test = []
    # result_verginica = []

    for x1,x2,x3 in zip(setosa_test,versicolor_test,verginica_test):
        temp1 ={}
        temp1[0]=multivariate_normal.pdf(x1, mean=xMean1, cov=covX1);
        temp1[1]=multivariate_normal.pdf(x1, mean=xMean2, cov=covX2);
        temp1[2]=multivariate_normal.pdf(x1, mean=xMean3, cov=covX3);
        res1 = max(temp1.items(), key=operator.itemgetter(1))[0]
    #     print(res1)
        ans_setosa_test.append(res1)
        
        
        temp2 ={}
        temp2[0]=multivariate_normal.pdf(x2, mean=xMean1, cov=covX1);
        temp2[1]=multivariate_normal.pdf(x2, mean=xMean2, cov=covX2);
        temp2[2]=multivariate_normal.pdf(x2, mean=xMean3, cov=covX3);
        res2 = max(temp2.items(), key=operator.itemgetter(1))[0]
    #     print(res2)
        ans_versicolor_test.append(res2)
        
        
        temp3 ={}
        temp3[0]=multivariate_normal.pdf(x3, mean=xMean1, cov=covX1);
        temp3[1]=multivariate_normal.pdf(x3, mean=xMean2, cov=covX2);
        temp3[2]=multivariate_normal.pdf(x3, mean=xMean3, cov=covX3);
        res3 = max(temp1.items(), key=operator.itemgetter(1))[0]
    #     print(res3)
        ans_verginica_test.append(res3)
        pass

    print(ans_verginica_test,ans_versicolor_test,ans_setosa_test)

    sum1,sum2,sum3= 0,0,0;print(sum1,sum2,sum3)
    for res1,res2,res3 in zip(ans_setosa_test,ans_versicolor_test,ans_verginica_test):
        if res1 == 0:
            sum1 = sum1 + 1
        if res2 == 1:
            sum2 = sum2 + 1
        if res3 == 2:
            sum3 = sum3 + 1
        pass
    print(sum1,sum2,sum3)  
    acc1 = sum1 / 10
    acc2 = sum2 / 10
    acc3 = sum3 / 10
    accOverall = (sum1 + sum2 + sum3)/30
    valPlot = []
    valPlot.append(acc1)
    valPlot.append(acc2)
    valPlot.append(acc3)
    valPlot.append(accOverall)
    print(valPlot)
    labelPlot = ["Setosa","Versicolor","Verginica","Overal"]
    plt.scatter(labelPlot,valPlot,label="Accuracy vs Class",color="blue",s=40)
    plt.show()






Bayers()