#
# @lc app=leetcode id=80 lang=python3
# @lcpr version=30204
#
# [80] Remove Duplicates from Sorted Array II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        sz = 2
        for i in range(2, n):
            if nums[sz - 2] != nums[i]:
                nums[sz] = nums[i]
                sz += 1
        return min(sz, n)  # for n = 1
# @lc code=end






#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

