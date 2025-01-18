# @algorithm @lc id=446 lang=python3 
# @title arithmetic-slices-ii-subsequence


from en.Python3.mod.preImport import *
# @test([2,4,6,8,10])=7
# @test([7,7,7,7,7])=16
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # dp[i][d] 表示以 nums[i] 結尾，公差為 d 的等差數列的個數
        dp = [defaultdict(int) for _ in range(n)]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j] # 公差
                ans += dp[j][d]
                dp[i][d] += (dp[j][d] + 1)
        return ans