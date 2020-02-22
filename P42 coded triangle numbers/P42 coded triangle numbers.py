# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:01:02 2020

@author: manis
"""
import time
start_time = time.time()

with open('p042_words.txt', 'r') as file:
    data = file.read().replace('\n','')
    data = data.replace('"', '')
    data=data.split(',')
file.close()

trianglenumlist=[False]*1000
for i in range(1,40):
    trianglenumlist[int(i*(i+1)/2)]=True
no_of_triangle_words=0
for word in data:
    sum=0
    for x in word:
        sum+= (ord(x)-64)
    #print(sum)
    if trianglenumlist[sum]==True:
        no_of_triangle_words+=1
print(no_of_triangle_words)
print("Program run time(in s): ", (time.time() - start_time))



