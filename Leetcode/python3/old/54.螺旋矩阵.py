#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [0] * (m*n)
        DIRETION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        st = (0, 0)
        cd = 0 # current direction
        for i in range(m*n):
            ans[i] = matrix[st[0]][st[1]]
            matrix[st[0]][st[1]] = None
            nx, ny = st[0] + DIRETION[cd][0], st[1] + DIRETION[cd][1]
            # 模擬轉向，注意模擬到最後一個節點(中間點)後，就不用再轉向了
            while (nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] == None) and i < m*n-1:
                cd = (cd + 1) % 4
                nx, ny = st[0] + DIRETION[cd][0], st[1] + DIRETION[cd][1]
            st = (nx, ny)
        return ans
# @lc code=end

