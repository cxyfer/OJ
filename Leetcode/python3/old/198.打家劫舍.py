#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        # dp[i] 表示前i個房子能偷到的最大金額
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            # 1. 不選第i個 或 2. 選第i個
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i-1])
        return dp[n]
# @lc code=end

