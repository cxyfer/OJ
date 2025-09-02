"""
    Dynamic Programming
    dp[n][k] 代表 前i場比賽，選擇k場，Rating 的 第一項的分子的最大值
    dp[n][k] = max(dp[n-1][k], dp[n-1][k-1] * 0.9 + P[n])
    對於固定 k ， Rating 的第一項的分母和第二項都是固定的，所以只要找到最大的分子就好
"""
from math import sqrt

N = int(input())
P = list(map(int, input().split()))

# 分子
dp = [[-float('inf') for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
for n in range(1, N+1):
    for k in range(1, n+1):
        dp[n][k] = max(dp[n-1][k], dp[n-1][k-1] * 0.9 + P[n-1])

# 分母
nines = [0 for _ in range(N+1)]
nines[1] = 1
for k in range(2, N+1):
    nines[k] = nines[k-1] * 0.9 + 1

# Ans
ans = -float('inf')
for k in range(1, N+1):
    ans = max(ans , dp[N][k] / nines[k] - 1200 / sqrt(k))
print(ans)
