# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:24:57 2019

@author: manis
"""
def ispalin(N):
    digitsofN=[]
    n=N
    while(n!=0):
        digitsofN.append(n%10)
        n=int(n/10)
    #print(digitsofN)
    #print(len(digitsofN))
    a=digitsofN
    for i in range(0,len(a)):
        if(a[i]!=a[len(a)-i-1]):
            #print("Bingo",i)
            return 0
    return 1
x=ispalin(1243420)

largestpalin=1
for i in range(100,1000):
    for j in range(100,1000):
        if(i*j>largestpalin):
            if(ispalin(i*j)==1):
                largestpalin=i*j
