# @algorithm @lc id=198 lang=python3 
# @title house-robber


from en.Python3.mod.preImport import *
# @test([1,2,3,1])=4
# @test([2,7,9,3,1])=12
class Solution:
    """
        Dynamic Programming
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 表示前i個房子能偷到的最大金額
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            # 1. 不選第i個 或 2. 選第i個(下標為i-1)
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i-1]) 
        return dp[n]