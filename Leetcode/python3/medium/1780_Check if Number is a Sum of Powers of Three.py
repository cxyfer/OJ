#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = int(1e7 + 5)
POW3 = [1]
while POW3[-1] < MAX_N:
    POW3.append(POW3[-1] * 3)
POW3.reverse()

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for x in POW3:
            if n == x:
                return True
            if n > x:
                n -= x
        return n == 0
# @lc code=end

