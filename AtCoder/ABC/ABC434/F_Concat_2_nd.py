from itertools import pairwise
from functools import cmp_to_key


def solve():
    N = int(input())
    words = [input() for _ in range(N)]

    def cmp(x, y):
        xy = x + y
        yx = y + x
        return (xy > yx) - (xy < yx)

    words.sort(key=cmp_to_key(cmp))  # CPython AC, PyPy TLE

    class C(str):
        def __lt__(self, other):
            return self + other < other + self

    words.sort(key=C)  # CPython/PyPy AC

    if N == 2:
        words[-1], words[-2] = words[-2], words[-1]
        print("".join(words))
        return

    for w1, w2 in pairwise(words):
        if w1 + w2 == w2 + w1:  # e.g. ab + abab = abab + ab
            print("".join(words))
            return

    words[-1], words[-2] = words[-2], words[-1]
    ans1 = "".join(words)
    words[-1], words[-2] = words[-2], words[-1]
    words[-2], words[-3] = words[-3], words[-2]
    ans2 = "".join(words)
    print(min(ans1, ans2))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
