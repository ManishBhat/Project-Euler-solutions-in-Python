# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:01:04 2020

@author: manis
"""
import time
start_time = time.time()
import numpy as np


def returndigits(i):
    arr=np.zeros((10,), dtype=int)
    temp_i=i
    sum=0
    while(temp_i!=0):
        arr[temp_i%10]+=1
        temp_i=int(temp_i/10)
    return arr #Note that, no_of_digits=np.sum(arr)

list_of_pandigital_products=[]
for i in range(1,100):
    arr_i=returndigits(i)
    if max(arr_i)>1:
        continue #certified!
    j=102
    while True:
        arr_j=returndigits(j)
        k=i*j
        arr_k=returndigits(k)
        combined_arr=arr_i+arr_j+arr_k
        if np.sum(combined_arr)>9:
            break
        elif np.sum(combined_arr)==9:
            if combined_arr[0]==0 and np.max(combined_arr)==1:
                print(i,j,i*j)
                if i*j not in list_of_pandigital_products:
                    list_of_pandigital_products.append(i*j)
        j+=1
list_of_pandigital_products.sort()
print(list_of_pandigital_products)
print("The answer is: " ,str(sum(list_of_pandigital_products)))
print("Program run time(in s): ", (time.time() - start_time))