# @algorithm @lc id=1559 lang=python3 
# @title cherry-pickup-ii


from en.Python3.mod.preImport import *
# @test([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])=24
# @test([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])=28
class Solution:
    """
        Dynamic Programming
        dfs(i, j1, j2) 表示在第 i 行，機器人 1 在 j1 位置，機器人 2 在 j2 位置時，能夠摘到的最大櫻桃數
    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache # Memoization
        def dfs(i, j1, j2): # dfs(i, j1, j2) 表示在第 i 行，機器人 1 在 j1 位置，機器人 2 在 j2 位置時，能夠摘到的最大櫻桃數
            if i == m: return 0
            res = -float("inf")
            for y1 in [j1 - 1, j1, j1 + 1]: # y1, y2 各有 3 種可能的位置
                for y2 in [j2 - 1, j2, j2 + 1]:
                    if 0 <= y1 < n and 0 <= y2 < n and y1 != y2: # 在範圍內且不重疊
                        res = max(res, dfs(i + 1, y1, y2))
            return grid[i][j1] + grid[i][j2] + res
        return dfs(0, 0, n - 1)