# @algorithm @lc id=80 lang=python3 
# @title remove-duplicates-from-sorted-array-ii


from en.Python3.mod.preImport import *
# @test([1,1,1,2,2,3])=5
# @test([0,0,1,1,1,1,2,3,3])=7
class Solution:
    """
        Two pointers
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow = fast = 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # print(nums)
        return slow