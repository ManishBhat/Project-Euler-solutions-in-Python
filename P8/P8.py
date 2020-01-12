# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 01:46:18 2019

@author: manis
"""

f= open("P8.txt","r")
if f.mode=="r":
    contents=f.read()
    contents = [ x for x in contents if x.isdigit() ] #This line is for removing all non-numeric characters from string
    maxprod=1
    for i in range(1000-13):
        prod=1
        for j in range(13):
            prod=prod*int(contents[i+j])
        if prod>maxprod:
            maxprod=prod
    print(maxprod)
f.close()

