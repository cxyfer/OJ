"""
CSES-1750 Planets Queries I
https://cses.fi/problemset/task/1750/

TLE
"""

import sys
it = iter(sys.stdin.read().splitlines())
input = lambda: next(it)

def solve():
    n, q = map(int, input().split())
    m = 30
    A = list(map(lambda x: int(x) - 1, input().split()))

    pa = [[-1] * m for _ in range(n)]
    for u, v in enumerate(A):
        pa[u][0] = v

    for i in range(m - 1):
        for u in range(n):
            if pa[u][i] != -1:
                pa[u][i + 1] = pa[pa[u][i]][i]

    for _ in range(q):
        u, k = map(int, input().split())
        u -= 1
        while k:
            lb = k & -k
            u = pa[u][lb.bit_length() - 1]
            k &= k - 1
        print(u + 1)

if __name__ == "__main__":
    solve()