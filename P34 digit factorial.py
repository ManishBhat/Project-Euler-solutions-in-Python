# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:14:17 2020

@author: manis
"""
import time
start_time = time.time()

def fact(n):
    prod=1
    for i in range(1,n):
        prod*=(i+1)
    return prod
def digitfact(num,arr_fact):
    sum=0
    while(num!=0):
        sum+=arr_fact[num%10]
        num=int(num/10)
    return sum


arr_fact=[1]*10
for i in range(1,10):
    arr_fact[i]=fact(i)

sum=0    
for i in range(11,1000000):
    if digitfact(i,arr_fact)==i:
        print(i)
        sum+=i
print("The sum is: ",str(sum))
print("Program run time(in s): ", (time.time() - start_time))

