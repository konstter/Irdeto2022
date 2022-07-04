
def solution(A):

    def f(Ar):
        global c
        s_set, c1 = [], 0
        for n in Ar:
            if n:
                if n & 1:
                    c1 += 1
                s_set.append(n >> 1)
        if c1 > c:
            c = c1
        if c < len(s_set):
            f(s_set)

    f(A)


c = 0
# a_array = Array([0])
# a_array = Array([13, 7, 3])
# a_array = Array([2, 2])
a_array = [1, 2, 4, 8]
solution(a_array)
print(c)
