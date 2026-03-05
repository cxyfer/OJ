#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        def calc(b: int) -> int:
            res = 0
            for i, ch in enumerate(s):
                c = ord(ch) - ord('0')
                if c != (i & 1) ^ b:
                    res += 1
            return res
        return min(calc(0), calc(1))
# @lc code=end