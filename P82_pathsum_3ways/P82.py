# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:22:41 2020

@author: Manish
"""

def Q82():
    fhand = open("p082_matrix.txt","r")
    a = []
    for line in fhand:
        x = line.strip().split(',')
        a.append([int(j) for j in x])
    
    N = len(a)
    s = [[0]*N for i in range(N)]
    for i in range(N):
        s[i][0] = a[i][0]

    for j in range(1,N):
        s_arr = [0]
        for i in range(N):
            s_arr.append(s_arr[i]+a[i][j])
        for i in range(N):
            s[i][j] = s[i][j-1] + a[i][j]
            for k in range(N):
                val = s[k][j-1]
                if k<i:
                    val += s_arr[i+1] - s_arr[k]
                elif k==i:
                    val += a[k][j]
                else:
                    val += s_arr[k+1] - s_arr[i]
                if val < s[i][j]:
                    s[i][j] = val
    ans = s[0][N-1]
    for i in range(1, N):
        if s[i][N-1] < ans:
            ans = s[i][N-1]
    print(ans)
                
if __name__ == '__main__':
    import time
    start_time = time.time()
    Q82()
    print("Program run time(in s): ", (time.time() - start_time))
