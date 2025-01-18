# @algorithm @lc id=3093 lang=python3 
# @title sum-of-values-at-indices-with-k-set-bits


from en.Python3.mod.preImport import *
# @test([5,10,1,5,2],1)=13
# @test([4,3,2,1],2)=1
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            if bin(idx).count('1') == k:
                ans += num
        return ans