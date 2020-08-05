# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:35:27 2020

@author: Manish
"""
from math import log10

max_val = 0
ans = 0
fhand = open("p099_base_exp.txt")
n = 1
for line in fhand: 
    x,y = (int(i) for i in line.strip().split(',')) # Reading contents
    num = y*log10(x)
    if num > max_val:
        max_val = num
        ans = n
    n+=1
print(ans)