#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        cnts = [[0] * 26 for _ in range(2)]
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            cnts[i & 1][ord(ch1) - ord('a')] += 1
            cnts[i & 1][ord(ch2) - ord('a')] -= 1
        return all(v == 0 for cnt in cnts for v in cnt)
# @lc code=end

