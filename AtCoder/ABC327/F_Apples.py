"""
    Segment Tree
"""

from atcoder.lazysegtree import LazySegTree

N, D, W = map(int, input().split())
TX = [list(map(int, input().split())) for _ in range(N)]

mx = max([x for t, x in TX]) # 最大距離

LST = LazySegTree(max, 0, lambda x,y:x+y, lambda x,y:x+y, 0, [0] * (mx+W) )

TX.sort()
j = 0
ans = 0
for t, x in TX:
    LST.apply(x, x + W, 1)
    while j < N and TX[j][0] <= t - D:
        _, x2 = TX[j]
        LST.apply(x2, x2 + W, -1)
        j += 1
    ans = max(ans, LST.all_prod())

print(ans)
