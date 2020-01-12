# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 07:16:32 2019

@author: manis
"""
import time
start_time = time.time()

longest=1
terms=1
for i in range(1,1000000):
    j=i
    thisterm=1
    while j!=1:
        thisterm=thisterm+1

        if j%2==0:
            j=j/2
        else:
            j=3*j+1
    if thisterm>terms:
      terms=thisterm
      longest=i
print("Number with largest collatz sequence: ",longest)
print("Sequence length: ",terms)

print("Program run time(in s): ", (time.time() - start_time))
          