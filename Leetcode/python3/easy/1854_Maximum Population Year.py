#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_y = max(ed for _, ed in logs)
        diff = [0] * (max_y + 1)
        for st, ed in logs:
            diff[st] += 1
            diff[ed] -= 1
        ans = mx = s = 0
        for i in range(max_y + 1):
            s += diff[i]
            if s > mx:
                ans, mx = i, s
        return ans
# @lc code=end

