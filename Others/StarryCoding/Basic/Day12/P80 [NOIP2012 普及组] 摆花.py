from functools import cache

n, m = map(int, input().split())
A = list(map(int, input().split()))
MOD = int(1e6 + 7)

# @cache
# def dfs(i, j):
#     if i == n:
#         return 1 if j == 0 else 0
#     if j < 0:
#         return 0
#     res = 0
#     for k in range(A[i] + 1):
#         res = (res + dfs(i + 1, j - k)) % MOD
#     return res

# print(dfs(0, m))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(m + 1):
        for k in range(A[i] + 1):
            if j - k < 0:
                break
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j - k]) % MOD
print(dp[n][m])