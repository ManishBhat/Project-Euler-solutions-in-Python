# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:51:41 2020

@author: Manish
"""


def f(a,n, modulo):
    
    ans = a
    for i in range(1, n):
        ans = pow(a,ans, modulo)
    return ans
a = 1777
n = 1855
modulo = 10**8

print(f(a,n, modulo))
