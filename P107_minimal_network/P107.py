# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:43:50 2020

@author: Manish
"""
from py_alg_dat.graph import UnDirectedWeightedGraph
from py_alg_dat.graph_vertex import UnWeightedGraphVertex
from py_alg_dat.graph_algorithms import GraphAlgorithms

def getMatrix(fname):
    fhand = open(fname, "r")
    mat = []
    for line in fhand:
        arr = line.strip().split(",")
        for i in range(len(arr)):
            if arr[i] != "-":
                arr[i] = int(arr[i])
        mat.append(arr)
    return mat

mat = getMatrix("p107_network.txt")

n = len(mat)

graph = UnDirectedWeightedGraph(n)
vertex_list=[]
for i in range(n):
    x = UnWeightedGraphVertex(graph, str(i))
    graph.add_vertex(x)
    vertex_list.append(x)

print(vertex_list)
for i in range(n):
    for j in range(i, n):
        if mat[i][j]!= "-":
            graph.add_edge(vertex_list[i], vertex_list[j], mat[i][j])
    MST = GraphAlgorithms.kruskals_algorithm(graph)