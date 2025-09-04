#
# @lc app=leetcode id=3516 lang=python3
#
# [3516] Find Closest Person
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 0 if (d1 := abs(x - z)) == (d2 := abs(y - z)) else (1 if d1 < d2 else 2)
# @lc code=end

