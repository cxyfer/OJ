"""
    LeetCode 322. Coin Change
    1. 枚舉硬幣 -> 不排序也可以，但排序後可以更快
    2. 枚舉金額 -> TLE
"""

n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort() # 不排序不會影響答案，但排序後可以更快

# dp[i] 表示湊成 i 元的最小硬幣數
dp = [float("inf")] * (x + 1)
dp[0] = 0
for c in coins:
    for j in range(c, x + 1): # dp[j] 表示湊成 j 元的最小硬幣數，可以從 j - c 轉換過來
        dp[j] = min(dp[j], dp[j - c] + 1)
print(dp[x] if dp[x] != float("inf") else -1)