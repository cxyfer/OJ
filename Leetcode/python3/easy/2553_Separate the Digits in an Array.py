#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(c) for x in nums for c in str(x)]
# @lc code=end

