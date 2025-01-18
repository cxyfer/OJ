#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        # DP
        # dp[i] 表示前i個房子能偷到的最大金額
        x = self.cal(nums[1:]) # 不偷第一個房子
        y = self.cal(nums[:-1]) # 不偷最後一個房子
        return max(x, y)
        
    def cal(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            # 1. 不選第i個 或 2. 選第i個
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i-1])
        return dp[n]
# @lc code=end

