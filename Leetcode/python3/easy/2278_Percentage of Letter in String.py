#
# @lc app=leetcode id=2278 lang=python3
#
# [2278] Percentage of Letter in String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
# @lc code=end

