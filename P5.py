# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:44:54 2019

@author: manis
"""
import math


def f(n):
    ans=1
    for i in range(1,n+1):
        #print(n-i)
        ans=int(ans*i/math.gcd(ans,i))
    print(ans)
f(20)
        
        