# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:00:27 2020

@author: manis_4ol2faq
"""
import time
start_time = time.time()

Total_sum_of_numbers=0
for i in range(2,1000000):
    temp_i=i
    sum=0
    while(temp_i!=0):
        a=temp_i%10
        sum=sum+a**5
        temp_i=int(temp_i/10)
    if sum==i:
        Total_sum_of_numbers+=i
        print(i)
print("The answer is: " ,str(Total_sum_of_numbers))

print("Program run time(in s): ", (time.time() - start_time))