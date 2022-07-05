#!/usr/bin/python

def solution(A):
    global c
    s_set, c1 = [], 0
    for n in A:
        if n:
            if n & 1:
                c1 += 1
            s_set.append(n >> 1)
    if c1 > c:
        c = c1
    if c < len(s_set):
        solution(s_set)


c = 0
# a_array = Array([0])
# a_array = Array([13, 7, 3])
# a_array = Array([2, 2])
a_array = [1, 2, 4, 8]
solution(a_array)
print(c)
