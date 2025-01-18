# @algorithm @lc id=26 lang=python3 
# @title remove-duplicates-from-sorted-array


from en.Python3.mod.preImport import *
# @test([1,1,2])=2
# @test([0,0,1,1,1,2,2,3,3,4])=5
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        # Using fast and slow pointers
        fast, slow = 1, 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast] 
            fast += 1
        return slow+1
