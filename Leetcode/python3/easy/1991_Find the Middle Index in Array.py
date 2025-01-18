#
# @lc app=leetcode id=1991 lang=python3
# @lcpr version=30204
#
# [1991] Find the Middle Index in Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
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
# [2,3,-1,8,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,-1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,5]\n
# @lcpr case=end

#

