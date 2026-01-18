#
# @lc app=leetcode id=3813 lang=python3
#
# [3813] Vowel-Consonant Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = sum(ch in "aeiou" for ch in s)
        c = sum(ch.isalpha() and ch not in "aeiou" for ch in s)
        return math.floor(v / c) if c > 0 else 0
# @lc code=end

