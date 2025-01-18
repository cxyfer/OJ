s = input()
t = input()

m, n = len(s), len(t)

def solve1():
    # dp[i][j] 表示將 s[i:] 轉換為 t[j:] 的最小操作次數
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][n] = m - i
    for j in range(n + 1):
        dp[m][j] = n - j

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1

    print(dp[0][0])

def solve2():
    # dp[i][j] 表示將 s 的前 i 個字元轉換為 t 的前 j 個字元的最小操作次數
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    print(dp[m][n])

solve2()