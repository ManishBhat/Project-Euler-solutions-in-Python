# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:17:29 2020

@author: manis_4ol2faq
"""
import time
start_time = time.time()

lst=[]
counter=0
for a in range(2,101):
    for b in range(2,101):
        if a**b in lst:
            pass
        else:
            lst.append(a**b)
            counter+=1
            
print(counter)

print("Program run time(in s): ", (time.time() - start_time))
