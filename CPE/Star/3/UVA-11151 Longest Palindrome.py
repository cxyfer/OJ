"""
    Longest Palindrome Subsequence
    1. 轉換為 LCS 問題
    2. 區間 DP (Bottom-Up) 枚舉長度，由小區間到大區間
"""
T = int(input())

def solve1():
    s = input()
    t = s[::-1]
    n = len(s)
    f = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    print(f[n][n])

def solve2():
    s = input()
    n = len(s)
    if n == 0: # 特判輸入為空行的情況
        print(0)
        return
    f = [[0] * n for _ in range(n)]
    for i in range(n): # 初始化區間長度為 1 的值
        f[i][i] = 1
    for ln in range(2, n + 1): # 枚舉區間長度
        for i in range(n - ln + 1): # 枚舉區間左端點
            j = i + ln - 1 # 區間右端點
            if s[i] == s[j]:
                f[i][j] = f[i + 1][j - 1] + 2
            else:
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
    print(f[0][n - 1])

for _ in range(T):
    # solve1()
    solve2()