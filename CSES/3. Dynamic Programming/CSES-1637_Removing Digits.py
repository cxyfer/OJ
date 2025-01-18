"""
    DP，從可以刪除的數字轉移
"""
n = int(input())

dp = [float("inf")] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    # 枚舉可以刪除的數字
    for ch in str(i):
        if ch != '0':
            dp[i] = min(dp[i], dp[i - int(ch)] + 1)
print(dp[n])