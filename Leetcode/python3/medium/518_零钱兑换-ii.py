#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        DP
    """
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
# @lc code=end
sol = Solution()
print(sol.change(5, [1, 2, 5])) # 4
print(sol.change(3, [2])) # 0
print(sol.change(10, [10])) # 1
