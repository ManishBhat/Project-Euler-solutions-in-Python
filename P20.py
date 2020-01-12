# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 09:40:30 2019

@author: manis
"""
import math
N=1000
x=math.factorial(100)
print(x)
sum=0
while x!=0:
    sum=sum+x%10
    x=x//10
print(sum)