# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:58:12 2020

@author: manis
"""
import time
start_time = time.time()

def no_of_integer_right_triangles(p):
    num=0
    for c in range(int(p/3)+1,int(p/2)):
        for a in range(1,int(p/3)):
            b=p-c-a
            if a<b:
                if c*c==a*a+b*b:
                    num+=1
    return num
max_num=0
max_p=12
for p in range(12,1001):
    if max_num<no_of_integer_right_triangles(p):
        max_num=no_of_integer_right_triangles(p)
        max_p=p
print("The value of p ≤ 1000 for which the number of solutions is maximised is: ",max_p)
print("Program run time(in s): ", (time.time() - start_time))