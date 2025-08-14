#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = 1 << 31 - 1
MAX_3 = 1
while MAX_3 < MAX_N:
    MAX_3 *= 3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and MAX_3 % n == 0
# @lc code=end

