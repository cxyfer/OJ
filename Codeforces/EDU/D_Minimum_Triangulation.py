n = int(input())
V = [i for i in range(n + 1)] # 補 0

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][i] = 0
for i in range(1, n):
    dp[i][i + 1] = 0
for i in range(1, n - 1):
    dp[i][i + 2] = V[i] * V[i + 1] * V[i + 2]

for ln in range(4, n + 1):
    for l in range(1, n - ln + 2):
        r = l + ln - 1
        for k in range(l + 1, r):
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + V[l] * V[k] * V[r])
print(dp[1][n])
