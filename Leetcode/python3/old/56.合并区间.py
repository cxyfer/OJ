#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Greedy
        ans = []
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not ans or x > ans[-1][1]: # not overlap
                ans.append([x, y])
            else:
                ans[-1][1] = max(ans[-1][1], y) # overlap, update interval
        return ans
# @lc code=end

