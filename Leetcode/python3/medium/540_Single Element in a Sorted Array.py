#
# @lc app=leetcode id=540 lang=python3
# @lcpr version=30204
#
# [540] Single Element in a Sorted Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if mid ^ 1 < n and nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
# @lc code=end



#
# @lcpr case=start
# [1,1,2,3,3,4,4,8,8]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,7,7,10,11,11]\n
# @lcpr case=end

#

