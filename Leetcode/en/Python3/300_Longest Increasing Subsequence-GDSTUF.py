# @algorithm @lc id=300 lang=python3 
# @title longest-increasing-subsequence


from en.Python3.mod.preImport import *
# @test([10,9,2,5,3,7,101,18])=4
# @test([0,1,0,3,2,3])=4
# @test([7,7,7,7,7,7,7])=1
class Solution:
    """
        Dynamic Programming
        dp[i] 表示以 nums[i] 結尾的 LIS 長度
        dp[i] = max(dp[i], dp[j] + 1) for j in [0, i) if nums[j] < nums[i]
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        ans = 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(i): # 枚舉 i 前面的所有位置 j
                if nums[j] < nums[i]: # nums[i] 可以接在 nums[j] 後面
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans