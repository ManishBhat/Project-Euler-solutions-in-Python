# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 04:41:52 2019

@author: manis
"""
import time
start_time = time.time()

def collatz(N,collatz_arr):
    n=int(N)
    while(1):
        if n<len(collatz_arr):
            #print("fasf")
            if collatz_arr[n]!=0:
                #print('JOL')
                return collatz_arr[n]
        if n%2==0:
            #print('SADDy')
            x=collatz(n/2,collatz_arr)+1
            if n<len(collatz_arr):
                collatz_arr[n]=x
            return x
        else:
            #print('HEssad')
            x=collatz(3*n+1,collatz_arr)+1
            if n<len(collatz_arr):
                collatz_arr[n]=x
            return x
            

N=1000000
collatz_arr=[0]*100000
collatz_arr[1]=1
maxcollatz=1
maxn=1
#print('HI')
'''
for n in range(1,100):
    #print('HER',n)
    print(n,collatz(n,collatz_arr))
    #print('YES',n)
'''
for n in range(1,N):
    if collatz(n,collatz_arr)>maxcollatz:
        maxcollatz=collatz(n,collatz_arr)
        maxn=n
print("Number with largest collatz sequence: ",maxn)
print("Sequence length: ",maxcollatz)

print("Program run time(in s): ", (time.time() - start_time))
