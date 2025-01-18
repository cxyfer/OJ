"""
    Dynamic Programming + 預處理
    dp[i] 表示和為i的完全平方數的最小個數
"""
N = 10000
t = int(input())
dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = i # i = (1^2) * i
    for j in range(1, int(i ** 0.5) + 1): # j*j <= i
        dp[i] = min(dp[i], dp[i - j * j] + 1)

for _ in range(t):
    n = int(input())
    print(dp[n])