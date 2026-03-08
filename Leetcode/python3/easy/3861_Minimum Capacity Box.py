#
# @lc app=leetcode id=3861 lang=python3
#
# [3861] Minimum Capacity Box
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1
        for i, c in enumerate(capacity):
            if c >= itemSize and (ans == -1 or c < capacity[ans]):
                ans = i
        return ans
# @lc code=end

