N, S, M, L = map(int, input().split())

MAX_N = N + 12
dp = [float("inf")] * (MAX_N+1) # dp[i]表示購買i個雞蛋所需的最小花費
dp[0], dp[6], dp[8], dp[12] = 0, S, M, min(L, S * 2)
for i in range(13, MAX_N+1):
    dp[i] = min(dp[i - 6] + S, dp[i - 8] + M, dp[i - 12] + L)
print(min(dp[N:MAX_N+1]))
