# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:15:37 2020

@author: manis_4ol2faq
"""

'''
def f(n,arr): #Function returning coin sums for value of n
    if n<0:
        return 0
    elif n==0:
        return 1 
    elif arr[n]!=-1:
        return arr[n]
    else:
        x=f(n-1,arr)+f(n-2,arr)+f(n-5,arr)+f(n-10,arr)+f(n-20,arr)+f(n-50,arr)+f(n-100,arr)+f(n-200,arr)
        arr[n]=x
        return x
arr=[-1]*300
print(f(200,arr))
'''

coin_list=[5,2,1]
n=10
i=0
for xi in range(len(coin_list)):
    temp_n=n-xi*i
    
    
            
