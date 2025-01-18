#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
# @lc code=start
import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS
        M, N = len(mat), len(mat[0])
        ans = [[0] * N for _ in range(M)]
        visited = [[False] * N for _ in range(M)]
        queue = collections.deque()
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < M and 0 <= new_y < N and not visited[new_x][new_y]:
                    ans[new_x][new_y] = ans[x][y] + 1
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
        return ans
    
# @lc code=end

