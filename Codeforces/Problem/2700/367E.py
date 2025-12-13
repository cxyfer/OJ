"""
CF367E - Sereja and Intervals
https://codeforces.com/problemset/problem/367/E

Open and Close Interval Trick
https://codeforces.com/blog/entry/47764
"""

from functools import reduce

MOD = int(1e9 + 7)

def solve():
    n, m, x = map(int, input().split())

    if n > m:
        print(0)
        return

    # f[i][j][k] 表示：考慮到第 i 個坐標，已選了 j 個左端點，k 個右端點的方案數
    f = [[0] * (n + 1) for _ in range(n + 1)]
    f[0][0] = 1

    for i in range(1, m + 1):
        nf = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(min(i, n) + 1):
            for k in range(j + 1):
                v = f[j][k] % MOD
                if not v: continue
                # 1. 什麼都不做
                if i != x:
                    nf[j][k] += v
                # 2. 放一個左端點
                if j + 1 <= n:
                    nf[j + 1][k] += v
                # 3. 放一個右端點
                if i != x and k + 1 <= j:
                    nf[j][k + 1] += v
                # 4. 同時放左端點和右端點
                if j + 1 <= n:
                    nf[j + 1][k + 1] += v
        f = nf

    # 最終答案為 f[n][n] * n!
    print(f[n][n] * reduce(lambda x, y: x * y % MOD, range(1, n + 1)) % MOD)

if __name__ == '__main__':
    solve()
