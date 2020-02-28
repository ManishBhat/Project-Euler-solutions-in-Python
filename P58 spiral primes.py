# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:25:10 2020

@author: manis_apezuzf
"""

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

N=10
for n in range(2,N):
    a1=4*n*n-10*n+7
    sieveoferat