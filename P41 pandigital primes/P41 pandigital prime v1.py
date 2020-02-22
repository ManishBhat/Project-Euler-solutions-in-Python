# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:41:10 2020

@author: manis
"""
import time
start_time = time.time()

def f(n):   #This code will find the sum of all primes below n
    sieveoferat=[True]*n
    sieveoferat[0]=sieveoferat[1]=False
    listofprimes=[]
    for i in range(2,n):
        if(sieveoferat[i]==True):
            listofprimes.append(i)
            j=2
            while(j*i<n):
                sieveoferat[j*i]=False
                j=j+1
    return sieveoferat

sieveoferat=f(7654322)
from itertools import permutations

lst=[''.join(p) for p in permutations("1234567")]

for i in reversed(lst):
    if sieveoferat[int(i)]==True:
        print(i)
        break
print("Program run time(in s): ", (time.time() - start_time))