# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:54:19 2020

@author: Manish
"""
import numpy as np

def Q78():
    """
    This code at present is too slow. To solve this I need to use the math
    theory of integer partitions.
    """
    N = 10_000
    #arr = np.zeros(shape=(N+1,N+1),dtype=int)
    arr = [[0]*(N+1) for i in range(N+1)]
    
    for j in range(N+1):
        arr[0][j] = arr[1][j] = 1
    arr[1][0] = 0
    for i in range(N+1):
        arr[i][1] = 1
    
    for i in range(2, N+1):
        for j in range(2, N+1):
            if i - j >= 0:
                arr[i][j] = arr[i][j-1] + arr[i-j][j]
            else:
                arr[i][j] = arr[i][j-1]
            arr[i][j] %= 1_000_000
    for n in range(2, N+1):
        if arr[n][n] % 1_000_000 == 0:
            print(n)  # Our answer!
            break

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q78()
    print("Program run time(in s): ", (time.time() - start_time)) 