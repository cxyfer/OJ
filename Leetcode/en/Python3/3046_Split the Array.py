# @algorithm @lc id=3324 lang=python3 
# @title split-the-array


from en.Python3.mod.preImport import *
# @test([1,1,2,2,3,4])=true
# @test([1,1,1,1])=false
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        return all(v <= 2 for v in cnt.values())
        