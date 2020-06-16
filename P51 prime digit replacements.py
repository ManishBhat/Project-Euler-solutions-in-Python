# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:25:39 2020

@author: Manish
"""
import time


from itertools import permutations


def unique_perms(series):
    return {"".join(p) for p in permutations(series)}


def main():
    a = {1:3,2:4}
    b = {2,3}
    print(type(b))
    print(a.values())
    print(sorted(unique_perms('1122')))


if __name__ == '__main__':
    starttime = time.time()
    main()
    print("Program time(in s) : ", time.time()-starttime)
