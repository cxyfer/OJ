# @algorithm @lc id=1349 lang=python3 
# @title check-if-it-is-a-straight-line


from en.Python3.mod.preImport import *
# @test([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])=true
# @test([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])=false
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0
        for x, y in coordinates[2:]:
            if dy * (x - x0) != dx * (y - y0):
                return False
        return True