#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # return reduce(lambda x, y: ((x << y.bit_length()) | y) % MOD, range(1, n + 1))
        ans = 0
        for i in range(1, n + 1):
            ans = ((ans << (i.bit_length())) | i) % MOD
        return ans
# @lc code=end

