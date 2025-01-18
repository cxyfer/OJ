# @algorithm @lc id=2767 lang=python3 
# @title maximum-sum-with-exactly-k-elements


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],3)=18
# @test([5,5,5],2)=11
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (k-1) * k // 2