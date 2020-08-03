# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 08:29:53 2020

@author: Manish
"""


def Q81():
    fhand = open("p081_matrix.txt","r")
    N = 80
    a = [[0]*N for i in range(N)]
    S = [[0]*N for i in range(N)]
    i = 0
    for line in fhand:
        x = line.strip().split(',')
        a[i] = [int(j) for j in x]
        i += 1
    S[0][0] = a[0][0]
    for i in range(1,N):
        S[0][i] = S[0][i-1] + a[0][i]
        S[i][0] = S[i-1][0] + a[i][0]
    for i in range(1,N):
        for j in range(1,N):
            S[i][j] = min(S[i-1][j], S[i][j-1]) + a[i][j]
    print(S[N-1][N-1])

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q81()
    print("Program run time(in s): ", (time.time() - start_time)) 