# @algorithm @lc id=27 lang=python3 
# @title remove-element


from en.Python3.mod.preImport import *
# @test([3,2,2,3],3)=2
# @test([0,1,2,2,3,0,4,2],2)=5
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        # Using fast and slow pointers
        fast, slow = 0, 0
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast] 
                slow += 1
            fast += 1
        return slow