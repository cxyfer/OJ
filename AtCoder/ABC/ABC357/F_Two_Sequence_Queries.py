"""
    Lazy Segment Tree
"""
from atcoder.lazysegtree import *
MOD = 998244353

def op(x,y):
    return x[0] + y[0], (x[1] + y[1]) % MOD, (x[2] + y[2]) % MOD, (x[3] + y[3]) % MOD
def mapping(l,e):
    return e[0], (e[1] + l[0] * e[0]) % MOD, (e[2] + l[1] * e[0]) % MOD, (e[3] + e[1] * l[1] + e[2] * l[0] + l[0] * l[1] * e[0]) % MOD
def composition(x,y):
    return (x[0] + y[0]) % MOD, (x[1] + y[1]) % MOD

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

seg = LazySegTree(op, (1, 0, 0, 0), mapping, composition, (0, 0), [(1, i, j, i * j) for i, j in zip(A, B)])
for _ in range(Q):
    op, *args = map(int, input().split())
    if op == 3:
        l, r = args
        print(seg.prod(l - 1, r)[3] % MOD)
    else:
        l, r, x = args
        seg.apply(l - 1, r, (x, 0) if op == 1 else (0, x))