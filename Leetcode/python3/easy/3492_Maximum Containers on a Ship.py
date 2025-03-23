#
# @lc app=leetcode id=3492 lang=python3
#
# [3492] Maximum Containers on a Ship
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)
# @lc code=end

