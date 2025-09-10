"""
P3961 [TJOI2013] 黄金矿工
https://www.luogu.com.cn/problem/P3961
分組背包，由於相同直線上必須從前到後收集，所以一定是選前 k 個。
注意題目的範圍，點一定是在第一象限和第二象限，因此相同斜率的直線只有一個前進方向。
且前後關係只需要對 y 座標由小到大排序即可。
"""
from collections import defaultdict
import math
def solve():
    n, T = map(int, input().split())
    groups = defaultdict(list)
    for _ in range(n):
        x, y, t, v = map(int, input().split())
        g = math.gcd(x, y)
        groups[(x // g, y // g)].append((x, y, t, v))
    f = [0] * (T + 1)
    for _, g in groups.items():
        g.sort(key=lambda x: x[1])
        items = []
        st = sv = 0
        for _, _, t, v in g:
            st += t
            sv += v
            items.append((st, sv))
        for j in range(T, -1, -1):
            for st, sv in items:
                if j >= st:
                    f[j] = max(f[j], f[j - st] + sv)
    print(f[T])

if __name__ == "__main__":
    solve()