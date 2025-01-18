# @algorithm @lc id=377 lang=python3 
# @title combination-sum-iv


from en.Python3.mod.preImport import *
# @test([1,2,3],4)=7
# @test([9],3)=0
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for idx in range(1, target+1):
            for num in nums:
                if idx >= num:
                    dp[idx] += dp[idx-num]
        return dp[-1]