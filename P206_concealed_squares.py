# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:56:50 2020

@author: Manish
"""
import time

def confirm(n):
    x = str(n*n)
    for i in range(1,9):
        if x[2*i] != str(i+1):
            return False
    return True


def Q206():
    n1 = 1009950490
    n2 = 1389244400

    i = 1389244370
    j = 1389244330
    while i<n2:
        if confirm(i):
            print(i)
            break
        if confirm(j):
            print(j)
            break
        i-=100
        j-=100


if __name__ == '__main__':
    start_time = time.time()
    Q206()
    print("Run time(in s): ", time.time() - start_time)