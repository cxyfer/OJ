# You are at a fruit market with different types of exotic fruits on display.

# You are given a 1-indexed array prices, where prices[i] denotes the number of coins needed to purchase the ith fruit.

# The fruit market has the following offer:

# If you purchase the ith fruit at prices[i] coins, you can get the next i fruits for free.
# Note that even if you can take fruit j for free, you can still purchase it for prices[j] coins to receive a new offer.

# Return the minimum number of coins needed to acquire all the fruits.

from typing import List

class Solution:
    """
        Dynamic Programming
        dp[i][j] 表示買i個水果的最小花費，第j個水果是否買
        - dp[i][1] = min(dp[i-1][1] , dp[i-1][0]) + prices[i]
        - 如果前k個有買，那這個可以不買
          k + k <= i => k <= i//2
        
    """
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        dp = [[float("inf")] * (2) for _ in range(n + 1)]
        # dp[0][0] = dp[0][1] = 0 # 
        dp[1][1] = prices[0] # 第一個水果一定要買
        for i in range(2, n + 1):
            dp[i][1] = min(dp[i-1][1] , dp[i-1][0]) + prices[i-1]
            for k in range(1, i//2+1):
                dp[i][0] = min(dp[i][0], dp[i-k][1])
        return min(dp[n][0], dp[n][1])
sol = Solution()
print(sol.minimumCoins([3,1,2])) # 4
print(sol.minimumCoins([1,10,1,1])) # 2
print(sol.minimumCoins([26,18,6,12,49,7,45,45])) # 39