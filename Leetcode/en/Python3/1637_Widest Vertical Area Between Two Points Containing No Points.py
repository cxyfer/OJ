# @algorithm @lc id=1742 lang=python3 
# @title widest-vertical-area-between-two-points-containing-no-points


from en.Python3.mod.preImport import *
# @test([[8,7],[9,9],[7,4],[9,7]])=1
# @test([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])=3
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[0])
        ans = 0
        for i in range(1, n):
            ans = max(ans, points[i][0] - points[i - 1][0])
        return ans