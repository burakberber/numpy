#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:35:39 2019

@author: burak
"""


import numpy as np#import lib



array = np.array([1,2,3,4,5,6,7,8,9]) #Creating a 1*9 array  


print(array.size) #Finding the size of an array


a = array.reshape(3,3) #Creating a 3*3 matrix


print("matrix:",a) #Printing matrix


print(a.T)# transpose of matrix 


print(a.mean())# finding mean


print(a.var())# finding variance


print(a.std())# finding standart deviation


print(a.max()) # finding max value


print(a.min()) # finding min value


print(a.sum())# finding sum

array2 = np.array([[189,27,6,54],[52,647,78,12],[922,837,83,42]])#Creating a matrix

print(np.zeros((4,4)))#Creating a 4X4 array with all zeros 

print(np.eye(4))#Creating 4*4 identity matrix.

print(np.ones((4,4))) #an array filled with ones.

a = np.array([5,2,7]) #creating arrays
b = np.array([3,9,1])

print(a+b)#sum of matrices

print(a-b)#subtraction of matrices

print(a**2)# square each element

print(a*b)#multiplying the same row and columns of matrix(not multiplying matrices!)

c = a.dot(b)#multiplying matrices
print(c)


