"""
P1704 寻找最优美做题曲线
https://www.luogu.com.cn/problem/P1704
分段求 LIS
"""
from itertools import pairwise
from bisect import bisect_left

def solve():
    N, K = map(int, input().split())
    P = [0] + list(map(int, input().split())) + [N + 1]
    C = [0] + list(map(int, input().split())) + [float('inf')]
    P.sort()

    for a, b in pairwise(P):
        if C[a] >= C[b]:
            print("impossible")
            return

    ans = K
    for l, r in pairwise(P):
        f = []
        for i in range(l + 1, r):
            if C[i] <= C[l] or C[i] >= C[r]:
                continue
            idx = bisect_left(f, C[i])
            if idx == len(f):
                f.append(C[i])
            else:
                f[idx] = C[i]
        ans += len(f)
    print(ans)

solve()