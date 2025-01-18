# @algorithm @lc id=3193 lang=python3 
# @title maximum-strong-pair-xor-i


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=7
# @test([10,100])=0
# @test([5,6,25,30])=7
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                x, y = nums[i], nums[j]
                if abs(x-y) <= min(x, y):
                    ans = max(ans, x^y)
        return ans