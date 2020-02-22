# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:21:19 2020

@author: manis
"""
import time
start_time = time.time()

i=1
chapernowne_const="."
while(len(chapernowne_const)<=1000001):
    chapernowne_const+=str(i)
    i+=1
d1=int(chapernowne_const[1])
d10=int(chapernowne_const[10])
d100=int(chapernowne_const[100])
d1000=int(chapernowne_const[1000])
d10000=int(chapernowne_const[10000])
d100000=int(chapernowne_const[100000])
d1000000=int(chapernowne_const[1000000])
print(d1*d10*d100*d1000*d10000*d100000*d1000000)
print("Program run time(in s): ", (time.time() - start_time))

