# @algorithm @lc id=3092 lang=python3 
# @title minimum-moves-to-spread-stones-over-grid


from en.Python3.mod.preImport import *
# @test([[1,1,0],[1,1,1],[1,2,1]])=3
# @test([[1,3,0],[1,0,0],[1,0,3]])=4
# @test([[1,2,2],[1,1,0],[0,1,1]])=4
# @test([[3,2,0],[0,1,0],[0,3,0]])=7

class Solution:
    """
        Backtrace
    """
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = [ (i, j) for i in range(n) for j in range(n) if grid[i][j] == 0]
        def solve(k): # 對第k個0進行處理，遞迴考慮下一個0
            if k == len(zeros):
                return 0
            x, y = zeros[k]
            res = float('inf')
            for i in range(3):
                for j in range(3):
                    if grid[i][j] > 1:
                        grid[i][j] -= 1 # 從(i,j)移動到(x,y)
                        res = min( solve(k+1)+abs(i-x)+abs(j-y), res) # 遞迴考慮下一個0
                        grid[i][j] += 1 # Backtrace
            return res
        return solve(0)