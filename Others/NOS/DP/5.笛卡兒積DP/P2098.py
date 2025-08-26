"""
P2098 [USACO16DEC] Team Building P
https://www.luogu.com.cn/problem/P2098
"""
MOD = int(1e9 + 9)
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

def solve1():  # Memoization (MLE)
    from functools import cache
    import sys
    sys.setrecursionlimit(int(5e3))
    @cache
    def f(i: int, j: int, k: int) -> int:
        if k == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        res = (f(i - 1, j, k) + f(i, j - 1, k) - f(i - 1, j - 1, k)) % MOD
        if A[i] > B[j]:
            res += f(i - 1, j - 1, k - 1)
            res %= MOD
        return res
    print(f(N - 1, M - 1, K))

def solve2a():  # 查表法 (MLE)
    f = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(M + 1):
            f[i][j][0] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            for k in range(1, K + 1):
                f[i][j][k] = (f[i - 1][j][k] + f[i][j - 1][k] - f[i - 1][j - 1][k]) % MOD
                if A[i - 1] > B[j - 1]:
                    f[i][j][k] += f[i - 1][j - 1][k - 1]
                    f[i][j][k] %= MOD
    print(f[N][M][K])

def solve2b():  # 查表法 (Rolling Array)
    f = [[[1] + [0] * K for _ in range(M + 1)] for _ in range(2)]
    for i in range(1, N + 1):
        cur, pre = i & 1, (i - 1) & 1
        for j in range(1, M + 1):
            for k in range(1, K + 1):
                f[cur][j][k] = (f[pre][j][k] + f[cur][j - 1][k] - f[pre][j - 1][k]) % MOD
                if A[i - 1] > B[j - 1]:
                    f[cur][j][k] += f[pre][j - 1][k - 1]
                    f[cur][j][k] %= MOD
    print(f[N & 1][M][K])

# solve1()
# solve2a()
solve2b()