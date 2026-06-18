#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        d1 = (hour % 12) * 30 + minutes * 0.5
        d2 = 6 * minutes
        d = abs(d1 - d2)
        return min(d, 360 - d)
# @lc code=end

