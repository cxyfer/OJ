# @algorithm @lc id=1635 lang=python3 
# @title number-of-good-pairs


from en.Python3.mod.preImport import *
# @test([1,2,3,1,1,3])=4
# @test([1,1,1,1])=6
# @test([1,2,3])=0
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        for idx, num in enumerate(nums):
            ans += cnt[num]
            cnt[num] += 1
        return ans