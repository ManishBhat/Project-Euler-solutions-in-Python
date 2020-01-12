# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 08:55:13 2019

@author: manis
"""
N=1000
x=2**N
print(x)
sum=0
while x!=0:
    sum=sum+x%10
    x=x//10
print(sum)