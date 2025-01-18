#
# @lc app=leetcode.cn id=2596 lang=python3
#
# [2596] 检查骑士巡视方案
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        DIR = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        n = len(grid)
        x, y = 0, 0
        for i in range(1, n*n):
            isValid = False
            for dx, dy in DIR:
                if 0 <= x+dx < n and 0 <= y+dy < n and grid[x+dx][y+dy] == i:
                    x, y = x+dx, y+dy
                    isValid = True
                    break
            if not isValid:
                return False
        return True
# @lc code=end
sol = Solution()
print(sol.checkValidGrid([[[8,3,6],[5,0,1],[2,7,4]]]))
