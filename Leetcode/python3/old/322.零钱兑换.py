#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from mod.preImport import *
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1]*amount # max amount of coins is amount+1
        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != (amount+1) else -1
# @lc code=end

