"""
P1435 [IOI 2000] 回文字串
https://www.luogu.com.cn/problem/P1435

等同將 s 變成 reverse(s) 的最小操作數
兩種思路：
- 令 f[i][j] 表示使 s[:i] 和 t[:j] 相等的最小操作數，由於操作是對稱的，所以答案為 f[n][n] // 2
- 令 f[i][j] 表示 s[:i] 和 t[:j] 的 LCS，則答案為 n - f[n][n]
"""
s = input()
t = s[::-1]
n = len(s)

def solve1a(s: str, t: str):  # 查表法
    s = " " + s
    t = " " + t
    f = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    f[0][0] = 0
    for i in range(1, n + 1):
        f[i][0] = i
    for j in range(1, n + 1):
        f[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            f[i][j] = min(f[i - 1][j] + 1,
                          f[i][j - 1] + 1,
                          f[i - 1][j - 1] + (s[i] != t[j]) * 2)
    print(f[n][n] // 2)

def solve1b(s: str, t: str):  # 刷表法
    s = " " + s + " "
    t = " " + t + " "
    f = [[float("inf")] * (n + 2) for _ in range(n + 2)]
    f[0][0] = 0
    for i in range(n + 1):
        for j in range(n + 1):
            si, tj = s[i + 1], t[j + 1]
            f[i + 1][j] = min(f[i + 1][j], f[i][j] + 1)
            f[i][j + 1] = min(f[i][j + 1], f[i][j] + 1)
            f[i + 1][j + 1] = min(f[i + 1][j + 1], f[i][j] + (si != tj) * 2)
    print(f[n][n] // 2)

def solve2a(s: str, t: str):  # 查表法
    # LCS
    f = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            f[i][j] = max(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1] + (s[i - 1] == t[j - 1]))
    print(n - f[n][n])

def solve2b(s: str, t: str):  # 刷表法
    # LCS
    s = " " + s + " "
    t = " " + t + " "
    f = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 1):
        for j in range(n + 1):
            f[i + 1][j] = max(f[i + 1][j], f[i][j])
            f[i][j + 1] = max(f[i][j + 1], f[i][j])
            f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + (s[i + 1] == t[j + 1]))
    print(n - f[n][n])

# solve1a(s, t)
# solve1b(s, t)
solve2a(s, t)
# solve2b(s, t)