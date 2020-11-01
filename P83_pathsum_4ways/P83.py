# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:56:30 2020

@author: Manish
"""

from dijkstar import Graph, find_path

def readfile():
    fhand = open("p083_matrix.txt","r")
    a = []
    for line in fhand:
        x = line.strip().split(',')
        a.append([int(j) for j in x])
    return a

def Q83():
    a = readfile()
    N = len(a)
    graph = Graph()
    for i in range(N):
        for j in range(N):
            if 0<= i-1<N:
                graph.add_edge(i*N + j, (i-1)*N + j, a[i-1][j])
            if 0<= i+1 <N:
                graph.add_edge(i*N + j, (i+1)*N + j, a[i+1][j])
            if 0<=j-1<N:
                graph.add_edge(i*N + j, i*N + j-1, a[i][j-1])
            if 0<=j+1<N:
                graph.add_edge(i*N + j, i*N + j+1, a[i][j+1])
    ans  = find_path(graph, 0 ,N**2-1).total_cost + a[0][0]
    print("The answer is:", ans)

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q83()
    print("Program run time(in s): ", (time.time() - start_time))