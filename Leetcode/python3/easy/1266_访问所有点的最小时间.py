#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#
from preImport import *
# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        cur = points[0]
        for i in range(1, n):
            nxt = points[i]
            ans += max(abs(nxt[0] - cur[0]), abs(nxt[1] - cur[1]))
            cur = nxt
        return ans
# @lc code=end

