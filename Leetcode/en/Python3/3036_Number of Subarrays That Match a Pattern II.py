# @algorithm @lc id=3290 lang=python3 
# @title number-of-subarrays-that-match-a-pattern-ii


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6],[1,1])=4
# @test([1,4,4,1,3,5,5,3],[1,0,-1])=2
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        