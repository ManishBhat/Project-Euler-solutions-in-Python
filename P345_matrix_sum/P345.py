# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:00:41 2020

@author: Manish
"""


def f(a):
    n = len(a)
    rowchosen = {}
    c = 0
    for r in range(n):
        rowchosen[frozenset([r])] = a[r][c]
    for c in range(1, n):
        newrow = dict()
        for x in rowchosen:
            range2 = frozenset(range(n)) - x
            for r in range2:
                s = frozenset().union(*[x, frozenset([r])])
                val = rowchosen[x] + a[r][c]
                if s not in newrow:
                    newrow[s] = val
                elif newrow[s] < val:
                    newrow[s] = val
        rowchosen = newrow
    #print(rowchosen)
    ans = list(rowchosen.values())[0]
    print("The answer is:", ans)


def Q345():
    fhand = open("matrix2.txt", "r")
    arr = []
    for line in fhand:
        arr.append([int(x) for x in line.split()])
    f(arr)


if __name__ == '__main__':
    import time
    start_time = time.time()
    Q345()
    print("Program run time(in s): ", (time.time() - start_time))
