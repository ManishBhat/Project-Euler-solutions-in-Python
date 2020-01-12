# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:11:48 2019

@author: manis
"""
#I am doing the amicable number problem

def d(N): #This function evaluates sum of divisors
    n=int(N)
    sum=1
    for i in range(2,n):
        if(n%i)==0:
            sum=sum+i
    return sum

#print(d(220),d(284))
print(d(6))
arr=[0]*100000
for n in range(1,10000):
   arr[n]=d(n)
for n in range(1,10000):
    if (arr[n]!=0 and arr[n]<10000 and arr[n]!=n):
        if arr[arr[n]]==n:
            print(n,arr[n])
        
        
    
