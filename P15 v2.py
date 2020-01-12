# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 08:03:06 2019

@author: manis
"""
import time
start_time = time.time()

import numpy as np

def numofways(r,d,arr): #With caching task gets done almost instantaneously
    if (arr[r,d]==0):
        arr[r][d]=numofways(r-1,d,arr)+numofways(r,d-1,arr)
    return arr[r][d]
def numofways2(r,d): #Without caching the same function takes enormous amount of time.
    if(r==0 or d==0):
        return 1
    else:
        return numofways2(r,d-1)+numofways2(r-1,d)

N=200


arr = np.zeros((N+1, N+1))
for i in range(N+1):
    arr[i][0]=arr[0][i]=1
print(numofways(N,N,arr))

#print(numofways2(N,N))


print("Program run time(in s): ", (time.time() - start_time))


    