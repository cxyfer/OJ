"""
P2758 编辑距离
https://www.luogu.com.cn/problem/P2758
"""

s = input()
t = input()

n, m = len(s), len(t)

def solve1(s: str, t: str):  # Memoization (MLE)
    from functools import cache
    @cache
    def f(i: int, j: int) -> int:
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        return min(f(i - 1, j) + 1, f(i, j - 1) + 1, f(i - 1, j - 1) + (s[i] != t[j]))
    print(f(n - 1, m - 1))

def solve2(s: str, t: str):  # 查表法
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        f[i][0] = i
    for j in range(m + 1):
        f[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1, f[i - 1][j - 1] + (s[i - 1] != t[j - 1]))
    print(f[n][m])

def solve3(s: str, t: str):  # 刷表法
    s = " " + s + " "
    t = " " + t + " "
    f = [[float("inf")] * (m + 2) for _ in range(n + 2)]
    f[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            f[i + 1][j] = min(f[i + 1][j], f[i][j] + 1)
            f[i][j + 1] = min(f[i][j + 1], f[i][j] + 1)
            f[i + 1][j + 1] = min(f[i + 1][j + 1], f[i][j] + (s[i + 1] != t[j + 1]))
    print(f[n][m])

# solve1(s, t)
# solve2(s, t)
solve3(s, t)