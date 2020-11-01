# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:39:40 2020

@author: Manish
"""

def Q104():
    n = 9
    #f = [0,1,1]
    fdigs = [0,1,1]
    ldigs = [0,1,1]
    k=3
    while True:
        fdigs.append(fdigs[k-1]+fdigs[k-2])
        ldigs.append(ldigs[k-1]+ldigs[k-2])
        #f.append(f[k-1]+f[k-2])
        ldigs[k] = int(str(ldigs[k])[-n:])
        #print(k, ldigs[k], f[k])
        #print(k, ldigs[k])
        if fdigs[k] > 10**n:
            fdigs[k]/=10
            fdigs[k-1]/=10
        #print(k, f[k])
        #firstdigs = str(val)[:n]
        firstdigs = str(int(fdigs[k]))
        if ''.join(sorted(firstdigs)) == "123456789" and ''.join(sorted(str(ldigs[k]))) == "123456789":
            print(k)
            break
        k+=1
if __name__ == '__main__':
    import time
    start_time = time.time()
    Q104()
    print("Program run time(in s): ", (time.time() - start_time))