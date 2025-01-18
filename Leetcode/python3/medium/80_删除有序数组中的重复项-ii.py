#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#
from preImport import *
# @lc code=start
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
# @lc code=end
# @test([1,1,1,2,2,3])=5
# @test([0,0,1,1,1,1,2,3,3])=7
sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3])) # 5
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3])) # 7