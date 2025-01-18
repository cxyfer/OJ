# @algorithm @lc id=213 lang=python3 
# @title house-robber-ii


from en.Python3.mod.preImport import *
# @test([2,3,2])=3
# @test([1,2,3,1])=4
# @test([1,2,3])=3
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