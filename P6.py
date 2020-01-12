# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 01:00:39 2019

@author: manis
"""
import math
def f(n):
    sumofsquares=int(n*(n+1)*(2*n+1)/6)
    sumofnum=int(n*(n+1)/2)
    return math.pow(sumofnum,2)-sumofsquares
x=f(100)