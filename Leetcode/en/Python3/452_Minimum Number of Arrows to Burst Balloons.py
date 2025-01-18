# @algorithm @lc id=452 lang=python3 
# @title minimum-number-of-arrows-to-burst-balloons


from en.Python3.mod.preImport import *
# @test([[10,16],[2,8],[1,6],[7,12]])=2
# @test([[1,2],[3,4],[5,6],[7,8]])=4
# @test([[1,2],[2,3],[3,4],[4,5]])=2
class Solution:
    """
        Greedy
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1]) # 依照 x_end 遞增排序
        right = points[0][1] # 貪婪，往右邊射
        ans = 1
        for x_start, x_end in points:
            if x_start > right:
                ans += 1
                right = x_end
        return ans