# @algorithm @lc id=3320 lang=python3 
# @title maximum-number-of-operations-with-the-same-score-i


from en.Python3.mod.preImport import *
# @test([3,2,1,4,5])=2
# @test([3,2,6,1,4])=1
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        target = nums[0] + nums[1]
        for i in range(2, n, 2):
            if i + 1 < n and nums[i] + nums[i + 1] == target:
                ans += 1
            else:
                break
        return ans