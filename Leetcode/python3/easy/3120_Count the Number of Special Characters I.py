#
# @lc app=leetcode id=3120 lang=python3
#
# [3120] Count the Number of Special Characters I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        vis = set(word)
        for ch in ascii_lowercase:
            if ch in vis and ch.upper() in vis:
                ans += 1
        return ans
# @lc code=end

