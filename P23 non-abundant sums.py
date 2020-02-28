# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:56:17 2019

@author: manis
"""
import math

def d(N): #This function evaluates sum of proper divisors
    n=int(N)
    sumofalldiv=1
    for i in range(2,int(math.sqrt(N))+1):
        primesum=1
        j=i
        while n%i==0:
            primesum=primesum+j
            j=j*i
            n=int(n/i)
            #print(primesum)
        sumofalldiv=sumofalldiv*primesum
    if(n!=1):
        sumofalldiv=sumofalldiv*(1+n)
    sumofpropdiv=sumofalldiv-N
    return sumofpropdiv
arr=[0]*30000    #It has 1 if it is an abundant number
arr2=[]
for n in range(1,28124):
    if(d(n)>n):
        arr[n]=1 #Creating list of abundant numbers
        arr2.append(n)
sum=0
for n in range(1,28124):
    sum=sum+n
    for x in arr2:
        if n<x:
            continue
        elif arr[n-x]==1:
            sum=sum-n
            break
print(sum)