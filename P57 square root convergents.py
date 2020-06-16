# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:33:25 2020

@author: manis_apezuzf
"""
import math
numer=3
denom=2
n=1
counter=0

for n in range(2,1001):
    temp_numer=numer
    numer=numer+2*denom
    denom=temp_numer+denom
    if int(math.log10(numer))>int(math.log10(denom)):
        #print(numer,denom,n)
        counter+=1
print(counter)