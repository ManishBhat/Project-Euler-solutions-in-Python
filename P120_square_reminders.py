# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:12:42 2020

@author: Manish
"""


ans = 0
for a in range(3,1001):
    ans += 2*a*((a-1) // 2)
print(ans)