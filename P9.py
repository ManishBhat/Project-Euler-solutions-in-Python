# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 02:03:02 2019

@author: manis
"""
n=1000
for i in range(1,n):
    for j in range(i,n-i):
        k=n-i-j
        if k*k==i*i+j*j:
            print(i,j,k)
            print(i*j*k)