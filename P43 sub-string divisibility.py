# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:35:48 2020

@author: manis
"""
import time
start_time = time.time()

import math
primeNumbers=(2,3,5,7,11,13,17)

from itertools import permutations
lst=[''.join(p) for p in permutations("0123456789")]

sum=0
for i in range(math.factorial(9),len(lst)):
    num=lst[i]
    opt="True"
    for j in range(1,8):
        if int(num[j:j+3])%primeNumbers[j-1]!=0:
            opt="False"
            break
    if opt=="True":
        print(num)
        sum+=int(num)
print("The sum of the all 0 to 9 pandigital numbers with this property is: ",sum)
print("Program run time(in s): ", (time.time() - start_time))

