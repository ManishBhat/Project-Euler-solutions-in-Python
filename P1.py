# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:57:56 2019

@author: manis
"""
sum=0
for i in range(1,10):
    if i%3==0 or i%5==0:
        sum=sum+i
print(sum)
