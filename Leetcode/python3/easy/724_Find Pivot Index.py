#
# @lc app=leetcode id=724 lang=python3
# @lcpr version=30204
#
# [724] Find Pivot Index
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        s = 0 # prefix sum
        for i, x in enumerate(nums):
            if 2 * s + x == tot:
                return i
            s += x
        return -1
# @lc code=end



#
# @lcpr case=start
# [1,7,3,6,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,-1]\n
# @lcpr case=end

#

