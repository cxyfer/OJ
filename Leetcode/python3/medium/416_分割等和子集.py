#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from preImport import *
# @lc code=start
class Solution:
    """
        0-1背包問題
    """
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        target = s // 2
        if n < 2 or s % 2 == 1 or max(nums) > target:
            return False
        # dp[i][j] 前i個數字能否組成和為j
        dp = [[False] * (target + 1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = True
        dp[1][nums[0]] = True
        for i in range(2, n+1):
            num = nums[i-1]
            for j in range(1, target+1): # 對於每個和 j
                dp[i][j] = dp[i-1][j] # 不選第i個數字
                if j >= num: # 選第i個數字，從前i-1個數字中能否選出和為j-num的子集轉移
                    dp[i][j] = dp[i][j] or dp[i-1][j-num]
        return dp[n][target]
# @lc code=end

