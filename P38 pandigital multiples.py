# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:33:31 2020

@author: manis
"""
import time
start_time = time.time()

max_pandigital="0"
for i in range(9,10000):
    n=0
    x=str(i)
    j=2
    while len(x)<=9:
        x+=str(i*j)
        if ''.join(sorted(x))=="123456789":
            print(i,j,x)
            if max_pandigital<x:
                max_pandigital=x
        j+=1
print("The largest 1 to 9 pandigital 9-digit number that can be formed \
as the concatenated product of an integer with (1,2, ... , n) \
where n > 1 is: ",max_pandigital)
print("Program run time(in s): ", (time.time() - start_time))      