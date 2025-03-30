#
# @lc app=leetcode id=2980 lang=python3
#
# [2980] Check if Bitwise OR Has Trailing Zeros
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(x & 1 ^ 1 for x in nums) >= 2
# @lc code=end

