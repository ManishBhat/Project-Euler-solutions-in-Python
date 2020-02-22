# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:50:24 2020

@author: manis_4ol2faq
"""

from math import log10, ceil

def recurring_cycle(x,d,do_you_want_cycle=False):
    arr = [False] * 1000
    cycle_counter=0
    while True:
        y=int(10**ceil(log10(d/x))*x)
        x=y%d
        if x==0 or arr[x]==True:
            return cycle_counter
        else:
            arr[x]=True
            #print(x)
            cycle_counter+=1

max_cycle=0    
max_d=2
for d in range(2,1000):
    temp_cycle=recurring_cycle(1, d)
    if max_cycle<temp_cycle:
        max_cycle=temp_cycle
        max_d=d
print("1/"+str(max_d)+" has the longest recurring cycle.")