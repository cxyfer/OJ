"""
AIsing Programming Contest 2020
E - Camel Train
https://atcoder.jp/contests/aising2020/tasks/aising2020_e
"""

from heapq import heappush, heappushpop
from collections import defaultdict


def solve():
    n = int(input())

    A = defaultdict(list)
    B = defaultdict(list)

    ans = 0
    for _ in range(n):
        k, l, r = map(int, input().split())
        if l > r:
            ans += r
            A[k].append(l - r)
        else:
            ans += l
            B[k].append(r - l)

    hp = []
    for k, ds in sorted(A.items()):
        for d in ds:
            ans += d
            if len(hp) < k:
                heappush(hp, d)
            else:
                ans -= heappushpop(hp, d)
    hp = []
    for k, ds in sorted(B.items(), reverse=True):
        k = n - k
        for d in ds:
            ans += d
            if len(hp) < k:
                heappush(hp, d)
            else:
                ans -= heappushpop(hp, d)

    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
