#
# @lc app=leetcode id=3856 lang=python3
#
# [3856] Trim Trailing Vowels
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        # return s.rstrip("aeiou")
        i = len(s) - 1
        while i >= 0 and s[i] in "aeiou":
            i -= 1
        return s[:i + 1]
# @lc code=end

