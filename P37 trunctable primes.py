# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:58:46 2020

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

def isTrunctablePrime(n,sieveoferat):
    if n<10:
        return False
    x=str(n)
    for i in range(len(x)):
        if sieveoferat[int(x[i:])]==False:
           return False
    for i in range(1,len(x)):
        if sieveoferat[int(x[:i])]==False:
            return False
    return True

N=1000000
sieveoferat=f(N)
sum=0
for i in range(11,N):
    if isTrunctablePrime(i,sieveoferat)==True:
        print(i)
        sum+=i
print("The sum of all truncatable primes is: ",sum)
print("Program run time(in s): ", (time.time() - start_time))