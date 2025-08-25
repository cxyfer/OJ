"""
P1140 相似基因
https://www.luogu.com.cn/problem/P1140
"""
W = [[5, -1, -2, -1, -3],
     [-1, 5, -3, -2, -4],
     [-2, -3, 5, -2, -2],
     [-1, -2, -2, 5, -1],
     [-3, -4, -2, -1, 0]]
mp = {"A": 0, "C": 1, "G": 2, "T": 3}

n, s = input().split()
m, t = input().split()
n, m = int(n), int(m)

def solve1(s: str, t: str):  # Memoization (AC)
    from functools import cache
    import sys
    sys.setrecursionlimit(int(1e4))

    ss = [0] * (n + 1)
    st = [0] * (m + 1)
    for i in range(n):
        ss[i + 1] = ss[i] + W[mp[s[i]]][4]
    for i in range(m):
        st[i + 1] = st[i] + W[4][mp[t[i]]]
    @cache
    def f(i: int, j: int) -> int:
        if i < 0:
            return st[j + 1]
        if j < 0:
            return ss[i + 1]
        return max(f(i - 1, j) + W[mp[s[i]]][4],
                   f(i, j - 1) + W[4][mp[t[j]]],
                   f(i - 1, j - 1) + W[mp[s[i]]][mp[t[j]]])
    print(f(n - 1, m - 1))

def solve2(s: str, t: str):  # 查表法
    s = " " + s
    t = " " + t
    f = [[float("-inf")] * (m + 1) for _ in range(n + 1)]
    f[0][0] = 0
    for i in range(1, n + 1):
        f[i][0] = f[i - 1][0] + W[mp[s[i]]][4]
    for j in range(1, m + 1):
        f[0][j] = f[0][j - 1] + W[4][mp[t[j]]]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            si, tj = mp[s[i]], mp[t[j]]
            f[i][j] = max(f[i - 1][j] + W[si][4],
                           f[i][j - 1] + W[4][tj],
                           f[i - 1][j - 1] + W[si][tj])
    print(f[n][m])

def solve3(s: str, t: str):  # 刷表法
    s = " " + s + "A"
    t = " " + t + "A"
    f = [[float("-inf")] * (m + 2) for _ in range(n + 2)]
    f[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            si, tj = mp[s[i + 1]], mp[t[j + 1]]
            f[i + 1][j] = max(f[i + 1][j], f[i][j] + W[si][4])
            f[i][j + 1] = max(f[i][j + 1], f[i][j] + W[4][tj])
            f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + W[si][tj])
    print(f[n][m])

# solve1(s, t)
solve2(s, t)
# solve3(s, t)