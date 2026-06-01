#
# @lc app=leetcode id=2580 lang=python3
#
# [2580] Count Ways to Group Overlapping Ranges
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
合併區間 + 快速冪
"""
# @lc code=start
MOD = int(1e9) + 7


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # 56. Merge Intervals
        ranges.sort()  # 按左端點排序
        cnt = 0
        last_r = -inf  # 維護最後一個區間的右端點
        for l, r in ranges:
            if l > last_r:
                cnt += 1
                last_r = r
            else:
                last_r = max(last_r, r)
        return pow(2, cnt, MOD)
# @lc code=end

