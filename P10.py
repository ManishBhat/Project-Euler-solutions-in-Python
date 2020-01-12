# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 02:09:53 2019

@author: manis
"""
import math
def f(N):   #This code will find the sum of all primes below N
    n=int(1.4*N)
    sieveoferat=[1]*n
    listofprimes=[]
    for i in range(2,n):
        if(sieveoferat[i]==1):
            listofprimes.append(i)
            j=2
            while(j*i<n):
                sieveoferat[j*i]=0
                j=j+1
    i=0
    sum=0
    while(listofprimes[i]<N): #summing all primes below N
        sum=sum+listofprimes[i]
        i=i+1
    return sum
print(f(2000000))