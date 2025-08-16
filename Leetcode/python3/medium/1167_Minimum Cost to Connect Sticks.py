#
# @lc app=leetcode id=1167 lang=python3
#
# [1167] Minimum Cost to Connect Sticks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            ans += x + y
            heappush(sticks, x + y)
        return ans
# @lc code=end

