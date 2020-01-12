# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 03:58:22 2019

@author: manis
"""
import math
f= open("P13.txt","r")
contents=[]
if f.mode=="r":
    for x in f.read().split():
        contents.append(int(x))
    f.close()
sum=0
for x in contents:
    sum=sum+x
print(sum)
ans=int(sum/pow(10,int(math.log10(sum)-10+1)))
print(ans)