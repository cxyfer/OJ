#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and n.bit_count() == 1
        return n > 0 and (n & -n) == n
        # return n > 0 and (n & (n - 1)) == 0
# @lc code=end

