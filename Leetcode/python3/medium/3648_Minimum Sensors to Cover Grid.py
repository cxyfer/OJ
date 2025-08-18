#
# @lc app=leetcode id=3648 lang=python3
#
# [3648] Minimum Sensors to Cover Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        sz = (2 * k + 1)
        return math.ceil(n / sz) * math.ceil(m / sz)
# @lc code=end

