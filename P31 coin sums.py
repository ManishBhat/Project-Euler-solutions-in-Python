# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:09:15 2020

@author: manis_apezuzf
"""

def main():
    import numpy as np
    coins=[1,2,5,10,20,50,100,200]
    N=200
    arr = np.zeros(shape=(N+1,len(coins)),dtype=int)
    
    for i in range(len(coins)):
        arr[0][i]=1
    for n in range(1,N+1):
        if n%coins[0]==0:
            arr[n][0]=1
        else:
            arr[n][0]=1
    for n in range(1,N+1):
        for i in range(1,len(coins)):
            for k in range(i+1):
                if n>=coins[k]:
                    arr[n][i]+=arr[n-coins[k]][k]
    print(arr[N,len(coins)-1])

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 