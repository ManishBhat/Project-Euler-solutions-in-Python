# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:22:41 2020

@author: Manish
"""

def Q81():
    """
    The algorithm used is incorrect.
    The problem is thus unsolved.
    """
    fhand = open("p082_matrix.txt","r")
    N = 80
    a = [[0]*N for i in range(N)]
    S = [[0]*N for i in range(N)]
    i = 0
    for line in fhand:
        x = line.strip().split(',')
        a[i] = [int(j) for j in x]
        i += 1
    for i in range(N):
        S[i][0] = a[i][0]
    for j in range(1,N):
        for i in range(N):
            if i == 0:
                S[i][j] = min(S[i][j-1], S[i+1][j-1] + a[i+1][j]) + a[i][j]
            elif i == N-1:
                S[i][j] = min(S[i-1][j-1]+a[i-1][j], S[i][j-1]) + a[i][j]
            else:
                S[i][j] = min(S[i-1][j-1]+a[i-1][j], S[i][j-1], S[i+1][j-1] + a[i+1][j]) + a[i][j]
    print(min([S[i][N-1] for i in range(N)]))


if __name__ == '__main__':
    import time
    start_time = time.time()
    Q81()
    print("Program run time(in s): ", (time.time() - start_time))
