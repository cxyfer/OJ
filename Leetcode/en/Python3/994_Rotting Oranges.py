# @algorithm @lc id=1036 lang=python3 
# @title rotting-oranges


from en.Python3.mod.preImport import *
# @test([[2,1,1],[1,1,0],[0,1,1]])=4
# @test([[2,1,1],[0,1,1],[1,0,1]])=-1
# @test([[0,2]])=0
class Solution:
    """
        BFS
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        ans = 0
        while q:
            x, y, step = q.popleft()
            ans = max(ans, step)
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    q.append((nx, ny, step + 1))
        for i in range(m): # 檢查是否還有新鮮橘子
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans