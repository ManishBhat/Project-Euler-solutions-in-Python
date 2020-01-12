# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 07:55:13 2019

@author: manis
"""
import time
start_time = time.time()

import math
print(int(math.factorial(40)/math.factorial(20)/math.factorial(20))) #The answer is 40!/(20!20!)

print("Program run time(in s): ", (time.time() - start_time))