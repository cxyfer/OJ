#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
from preImport import *
# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0
        for x, y in coordinates[2:]:
            if dy * (x - x0) != dx * (y - y0):
                return False
        return True
# @lc code=end

