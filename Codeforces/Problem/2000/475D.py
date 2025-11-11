"""
CF475D. CGCDSSQ
https://codeforces.com/problemset/problem/475/D

LogTrick
"""

import math
from collections import defaultdict

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    assert len(queries) == q

    cnt = defaultdict(int)
    gcds = []  # (區間 gcd，出現次數)
    for r, x in enumerate(A):
        # 維護以 r 為右端點的所有區間 gcd 值
        for p in gcds:
            p[0] = math.gcd(p[0], x)
        gcds.append([x, 1])

        # 原地去重，相同 gcd 值合併出現次數
        idx = 1
        for j in range(1, len(gcds)):
            if gcds[j][0] != gcds[idx - 1][0]:
                gcds[idx] = gcds[j]
                idx += 1
            else:
                gcds[idx - 1][1] += gcds[j][1]
        del gcds[idx:]

        for g, c in gcds:
            cnt[g] += c

    ans = [0] * q
    for i, x in enumerate(queries):
        ans[i] = cnt[x]
    print(*ans, sep='\n')

if __name__ == "__main__":
    solve()