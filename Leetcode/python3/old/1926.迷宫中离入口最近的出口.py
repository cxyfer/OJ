#
# @lc app=leetcode.cn id=1926 lang=python3
#
# [1926] 迷宫中离入口最近的出口
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        BFS
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        sx, sy = entrance
        q = deque([(sx, sy, 0)])
        maze[sx][sy] = '+'
        while q:
            x, y, step = q.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if nx == 0 or nx == m-1 or ny == 0 or ny == n-1:
                        return step + 1
                    maze[nx][ny] = '+'
                    q.append((nx, ny, step + 1))
        return -1
# @lc code=end
sol = Solution()
print(sol.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2]))
print(sol.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]],[1,0]))
