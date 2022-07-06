#!/usr/bin/python

def solution(A):

    def f(Ar, c):
        s_set, c1 = [], 0
        for n in Ar:
            if n:
                if n & 1:
                    c1 += 1
                s_set.append(n >> 1)
        if c1 > c:
            c = c1
        if c < len(s_set):
            return f(s_set, c)
        else:
            return c

    return f(A, 0)


# a_array = Array([0])
# a_array = Array([1, 2, 4, 8])
# a_array = Array([2, 2])
a_array = [13, 7, 3, 1]
print(solution(a_array))
