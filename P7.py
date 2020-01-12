# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 01:13:23 2019

@author: manis
"""
import math
def f(N):   #This code will find the Nth prime number
    n=int(1.4*N*math.log(N)) #The nth prime is around N*log(N)
    sieveoferat=[1]*n
    listofprimes=[]
    for i in range(2,n):
        if(sieveoferat[i]==1):
            listofprimes.append(i)
            j=2
            while(j*i<n):
                sieveoferat[j*i]=0
                j=j+1
    print(listofprimes)
    return listofprimes[N-1] #Note the 1st prime that is 2, is located at the 0th index. Thus, Nth prime will be at N-1
print(f(10001))