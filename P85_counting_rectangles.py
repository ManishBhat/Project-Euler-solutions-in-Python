# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:04:43 2020

@author: Manish
"""

def nC2(n):
    return (n*(n-1))//2

T = 2
min_err = 1_000_000
b,h = 0,0
while T < 1000:
    for t1 in range(1,T//2 + 1):
        t2 = T-t1
        val = nC2(t1+1)*nC2(t2+1)
        if abs(2_000_000 - val) < min_err:
            min_err = abs(2_000_000 - val)
            b,h = t1,t2
    T+=1
                
print(b,h, b*h, min_err)
print(nC2(b)*nC2(h))