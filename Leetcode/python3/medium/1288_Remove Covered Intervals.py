#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda p: (p[0], -p[1]))

        ans = n
        max_r = -inf
        for l, r in intervals:
            if r <= max_r:
                ans -= 1
            else:
                max_r = max(max_r, r)
        return ans
# @lc code=end

