#
# @lc app=leetcode id=3121 lang=python3
#
# [3121] Count the Number of Special Characters II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        pos = dict()
        for i, ch in enumerate(word):
            if ch.islower() or ch not in pos:
                pos[ch] = i
        ans = 0
        for ch in ascii_lowercase:
            if ch not in pos or ch.upper() not in pos:
                continue
            if pos[ch] < pos[ch.upper()]:
                ans += 1
        return ans
# @lc code=end

