#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:22:48 2020

@author: manish
"""

d = {}
i = 1

while i<10_000:
    mystr = ''.join(sorted(str(i**3)))
    d[mystr] = d.get(mystr, [])
    d[mystr].append(i)
    if len(d[mystr]) == 5:
        print(d[mystr])
    i+=1
print(f"Answer is: {5027**3}")