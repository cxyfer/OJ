# @algorithm @lc id=169 lang=python3 
# @title majority-element


from en.Python3.mod.preImport import *
# @test([3,2,3])=3
# @test([2,2,1,1,1,2,2])=2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.solve2(nums)
    """
        1. Hash Table
    """
    def solve1(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > len(nums)//2:
                return num
    """
        2. Boyer-Moore Voting Algorithm
    """
    def solve2(self, nums: List[int]) -> int:
        cnt = 0
        candidate = None
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if num == candidate else -1
        return candidate
            
        