# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:00:48 2020

@author: Manish
"""
import time

def ispalin(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

def Q125():
    N = 7071
    arr=[0]*N
    N2 = 10**8
    s = set()

    for i in range(1, N):
        arr[i] = arr[i-1] + i*i

    for i in range(N):
        for j in range(i+2, N):
            x = arr[j] - arr[i]
            if x >= N2:
                break
            if ispalin(x):
                s.add(x)

    print("Number of palins are:", len(s))
    print("Sum is:", sum(s))


if __name__ == '__main__':
    start_time = time.time()
    Q125()
    print("Program run time(in s): ", time.time() - start_time)