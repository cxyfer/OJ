# @algorithm @lc id=54 lang=python3 
# @title spiral-matrix


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=[1,2,3,6,9,8,7,4,5]
# @test([[1,2,3,4],[5,6,7,8],[9,10,11,12]])=[1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        DIRETION = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False] * n for _ in range(m)]
        x, y = 0, 0
        cd = 0 # current direction
        for i in range(m*n):
            ans.append(matrix[x][y])
            visited[x][y] = True
            nx, ny = x + DIRETION[cd][0], y + DIRETION[cd][1]
            # 模擬轉向
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                cd = (cd + 1) % 4
                nx, ny = x + DIRETION[cd][0], y + DIRETION[cd][1]
            x, y = nx, ny
        return ans