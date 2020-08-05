# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:17:01 2020

@author: Manish
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def sign (p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)


def PointInTriangle (pt, v1, v2, v3):
    '''
    Using half-plane method to determine if
    point lies in triangle.
    True if it does, False otherwise.
    '''
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not(has_neg and has_pos)


def Q102():
    fhand = open("p102_triangles.txt","r")
    counter = 0
    for line in fhand:
        val = [int(i) for i in (line.strip().split(","))]
        v1 = Point(val[0], val[1])
        v2 = Point(val[2], val[3])
        v3 = Point(val[4], val[5])
        pt = Point(0, 0)
        if PointInTriangle(pt, v1, v2, v3) is True:
            counter += 1
    print(counter)


if __name__ == '__main__':
    import time
    start_time = time.time()
    Q102()
    print("Program run time(in s): ", (time.time() - start_time)) 