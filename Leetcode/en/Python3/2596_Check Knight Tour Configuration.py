# @algorithm @lc id=2662 lang=python3 
# @title check-knight-tour-configuration


from en.Python3.mod.preImport import *
# @test([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]])=true
# @test([[0,3,6],[5,8,1],[2,7,4]])=false
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