# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:41:37 2020

@author: Manish
"""

def Q76():
    N = 100
    arr = [[0]*(N+1) for i in range(N+1)]
    for i in range(1, N+1):
        arr[0][i] = arr[1][i]= 1
    for i in range(N+1):
        arr[i][1] = 1

    for i in range(2, N+1):
        for j in range(2, N+1):
            if i - j >= 0:
                arr[i][j] = arr[i][j-1] + arr[i-j][j]
            else:
                arr[i][j] = arr[i][j-1]
    print(arr[N][N] - 1)

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q76()
    print("Program run time(in s): ", (time.time() - start_time))