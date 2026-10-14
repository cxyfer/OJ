#
# @lc app=leetcode id=3723 lang=python3
#
# [3723] Maximize Sum of Squares of Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if s > n * 9:
            return ""
        q, r = divmod(s, 9)
        return ('9' * q + (str(r) if r else '')).ljust(n, '0')
# @lc code=end

