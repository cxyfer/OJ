#
# @lc app=leetcode id=2546 lang=python3
#
# [2546] Apply Bitwise Operations to Make Strings Equal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
(0, 0) -> (0, 0)
(0, 1) -> (1, 1) => 0 -> 1
(1, 0) -> (1, 1) => 0 -> 1
(1, 1) -> (1, 0) => 1 -> 0
"""
# @lc code=start
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # return any(b != "0" for b in s) == any(b != "0" for b in target)
        return ("1" in s) == ("1" in target)
# @lc code=end

