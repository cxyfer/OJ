"""
    Knapsack DP
"""

n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

# dp[i] 表示花費價格為 i 時的所能獲得的最大頁數
dp = [0] * (x + 1)
for price, page in zip(prices, pages): # 枚舉每本書
    for j in range(x, price - 1, -1): # 枚舉轉移來源
        dp[j] = max(dp[j], dp[j - price] + page)
print(dp[x])