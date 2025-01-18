#
# @lc app=leetcode id=2270 lang=python3
# @lcpr version=30204
#
# [2270] Number of Ways to Split Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tot = sum(nums)
        s = list(accumulate(nums))
        return sum(2 * s[i] >= tot for i in range(len(nums) - 1))
# @lc code=end



#
# @lcpr case=start
# [10,4,-8,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1,0]\n
# @lcpr case=end

#

