# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:28:51 2020

@author: manis
"""
import time
start_time = time.time()

def is_palin(n): #Function to check if an integer n is a palindrome
    if str(n)==str(n)[::-1]:
        return True
    return False

N=1000000
sum=0  
for i in range(1,N):
    if is_palin(i):
        bin_rep=bin(i)[2:]
        if is_palin(bin_rep):
            print(i,bin_rep)
            sum+=i
print("The sum is:",sum)
print("Program run time(in s): ", (time.time() - start_time))
