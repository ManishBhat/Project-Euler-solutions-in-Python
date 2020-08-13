# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:38:22 2020

@author: Manish
"""

def nextnum(n):
    ans = 0
    while n!=0:
        ans += (n%10)**2
        n //= 10
    return ans

def Q92():
    N = 1_00_000
    #N = 10_000_000
    count89 = 0
    arr = [0]*N  # Records final value of square digit chain starting from i in arr[i]
    for i in range(1, N):
        if arr[i] == 89:
            count89 += 1
        elif arr[i] == 0:
            stack = []
            j = i
            while j != 1 and j != 89:
                stack.append(j)
                j = nextnum(j)
            for x in stack:
                arr[x] = j
            if j ==89:
                count89 += 1
                
    print(count89)
    
if __name__ == "__main__":
    import time
    start_time = time.time()
    Q92()
    print("Time taken (in s): ", time.time() - start_time)