#
# @lc app=leetcode id=26 lang=python3
# @lcpr version=30204
#
# [26] Remove Duplicates from Sorted Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = k = 0
        while (i < n):
            j = i
            while (i < n and nums[j] == nums[i]):
                i += 1
            nums[k] = nums[j]
            k += 1
        return k
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

