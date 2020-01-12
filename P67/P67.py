# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 09:16:17 2019

@author: manis
"""
import time
start_time = time.time()
import numpy as np

f = open('p067_triangle.txt', 'r')
# Read in all the lines of your file into a list of lines
lines_list = f.readlines()
# Does a double-nested list comprehension to get into the matrix
a=[[int(val) for val in line.split()] for line in lines_list[0:]]

N=100
sum = np.zeros((N, N))
for i in range(N):
    sum[N-1][i]=a[N-1][i]
for k in range(1,N+1):
    for i in range(0,N-k):
        sum[N-k-1][i]=a[N-k-1][i]+max(sum[N-k][i],sum[N-k][i+1])
print(sum[0][0])

print("Program run time(in s): ", (time.time() - start_time))