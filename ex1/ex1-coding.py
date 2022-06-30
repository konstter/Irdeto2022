
class Array:
    def __init__(self, A):
        self.A = A

    def solution(self):
        self.c = 0

        def f(Ar):
            s_set, c1 = [], 0
            for n in Ar:
                if n:
                    if n & 1:
                        c1 += 1
                    s_set.append(n >> 1)
            if c1 > self.c:
                self.c = c1
            if self.c < len(s_set):
                f(s_set)
        f(self.A)
        return self.c


if __name__ == '__main__':
    # a_array = Array([13, 7, 3])
    # a_array = Array([1, 2, 4, 8])
    # a_array = Array([2, 2])
    a_array = Array([0])
    print(a_array.solution())
