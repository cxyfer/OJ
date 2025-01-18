# @algorithm @lc id=260 lang=python3 
# @title single-number-iii


from en.Python3.mod.preImport import *
# @test([1,2,1,3,2,5])=[3,5]
# @test([-1,0])=[-1,0]
# @test([0,1])=[1,0]
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [num for num in cnt if cnt[num] == 1]