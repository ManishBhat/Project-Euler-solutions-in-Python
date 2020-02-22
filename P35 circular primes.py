# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:25:33 2020

@author: manis
"""

import time
start_time = time.time()

from math import log10, ceil

def f(n):   #This code will find the sum of all primes below N
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

N=1000000
sieveoferat=f(N)
arr=[-1]*N
for n in range(2,N):
    if sieveoferat[n]==False:
        continue
    arr[n]=1
    no_of_digits_in_n = ceil(log10(n))
    temp_n=n
    for i in range(no_of_digits_in_n):
        temp_n=int(temp_n%10)*(10**(no_of_digits_in_n-1))+int(temp_n/10)
        if sieveoferat[temp_n]==False or ceil(log10(temp_n)) !=no_of_digits_in_n:
            arr[n]=0
            break
no_of_circular_primes=0
for i in range(N):
    if arr[i]==1:
        print(i)
        no_of_circular_primes+=1
print("The no of circular primes smaller than one million are: ",no_of_circular_primes)
print("Program run time(in s): ", (time.time() - start_time))
