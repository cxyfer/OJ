# @algorithm @lc id=1395 lang=python3 
# @title minimum-time-visiting-all-points


from en.Python3.mod.preImport import *
# @test([[1,1],[3,4],[-1,0]])=7
# @test([[3,2],[-2,2]])=5
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