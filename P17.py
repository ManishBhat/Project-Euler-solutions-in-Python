# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:37:41 2020

@author: manis
"""

import numpy as np

arr=np.zeros(1001,dtype=np.uint16) #Creates an integer numpy array

arr[1]=arr[2]=3
arr[3]=5
arr[4]=arr[5]=4
arr[6]=3
arr[7]=arr[8]=5
arr[9]=4
arr[10]=3
arr[11]=arr[12]=6
arr[13]=arr[14]=8
arr[15]=arr[16]=7
arr[17]=9
arr[18]=arr[19]=8
arr[20]=arr[30]=6
arr[40]=arr[50]=arr[60]=5
arr[70]=7
arr[80]=arr[90]=6
arr[100]=7
arr[1000]=11

def f(n,arr): #return number of letters in numbers
    if n==100:
        return 10
    if n>1000:
        print("Error")
        return -123
    elif arr[n]!=0:
        return arr[n]
    elif n<100:
        return arr[n-n%10]+arr[n%10]
    elif n%100==0: #n=200,300,400,500,600,700,800,900
        return arr[int(n/100)]+arr[100]
    elif n>100:
        return arr[int(n/100)]+arr[100]+3+f(n%100,arr)
    else:
        print("Error 2")
        return(-435,n)

N=1000
sum=0
for i in range(1,N+1):
    print(i,f(i,arr))
    sum=sum+f(i,arr)
print(sum)
print(f(100,arr))