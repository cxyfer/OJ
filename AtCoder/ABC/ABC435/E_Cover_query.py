from itertools import pairwise
from atcoder.lazysegtree import LazySegTree

def solve():
    n, q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    Xs = set()
    for l, r in queries:  # [l, r] -> [l, r + 1)
        Xs.add(l)
        Xs.add(r + 1)
    
    Xs = sorted(Xs)
    mapX = {val: i for i, val in enumerate(Xs)}
    data = [(0, y - x) for x, y in pairwise(Xs)]  # (black_len, total_width)

    op = lambda a, b: (a[0] + b[0], a[1] + b[1])
    mapping = lambda f, s: (s[1], s[1]) if f == 1 else s
    composition = lambda f, g: f | g
    seg = LazySegTree(op, (0, 0), mapping, composition, 0, data)

    for l, r in queries:
        L, R = mapX[l], mapX[r + 1]
        seg.apply(L, R, 1)
        print(n - seg.all_prod()[0])

if __name__ == '__main__':
    solve()