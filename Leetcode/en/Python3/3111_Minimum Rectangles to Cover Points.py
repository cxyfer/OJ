# @algorithm @lc id=3390 lang=python3 
# @title minimum-rectangles-to-cover-points


from en.Python3.mod.preImport import *
# @test([[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]],1)=2
# @test([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]],2)=3
# @test([[2,3],[1,2]],0)=2
class Solution:
    """
        Greedy
        由於矩形的高度沒有限制，所以只要考慮橫座標即可。
        為使矩形數量最少，我們應該讓每個矩形的橫座標範圍盡可能大，
        因此對於最左邊的的點 (st, y) ，應該建立一個從 x = st 到 x = st + w 的矩形。
    """
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        n = len(points)
        points.sort(key = lambda x : x[0])
        ans = 0
        last = -float("inf")
        for x, y in points:
            if x > last:
                ans += 1
                last = x + w
        return ans