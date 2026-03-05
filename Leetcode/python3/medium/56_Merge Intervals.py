#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda p: p[0])  # sort by left endpoint
        for l, r in intervals:
            if not ans or l > ans[-1][1]:  # not overlap
                ans.append([l, r])
            else:
                ans[-1][1] = max(ans[-1][1], r)  # overlap, update interval
        return ans
# @lc code=end