# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:15:43 2019

@author: manis
"""
import math
N=600851475143
n=N
largestprimefactor=1
for i in range(2,int(math.sqrt(N))+1):
    while(n%i==0):
        n=n/i
        largestprimefactor=i
    if(n==1):
        break
if(n!=1):
    largestprimefactor=n