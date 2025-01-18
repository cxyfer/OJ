# @algorithm @lc id=3184 lang=python3 
# @title maximum-balanced-subsequence-sum


from en.Python3.mod.preImport import *
# @test([3,3,5,6])=14
# @test([5,-1,-3,8])=13
# @test([-2,-1])=-1
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        