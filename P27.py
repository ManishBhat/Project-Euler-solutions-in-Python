# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 01:21:02 2020

@author: manis
"""

def f(N):   #This code will find the sum of all primes below N
    n=int(1.4*N)
    sieveoferat=[True]*n
    listofprimes=[]
    for i in range(2,n):
        if(sieveoferat[i]==True):
            listofprimes.append(i)
            j=2
            while(j*i<n):
                sieveoferat[j*i]=False
                j=j+1
    return sieveoferat

N=2000000
sieveoferat=f(N)
max_n=0
max_a=0
max_b=0
for a in range(-999,1000):
    for b in range(-999,1000):
        n=0
        while True:
            if sieveoferat[n*n+a*n+b] == False:
                break
            n=n+1
        if n>max_n:
            max_n=n
            max_a=a
            max_b=b
print(max_a*max_b)
            