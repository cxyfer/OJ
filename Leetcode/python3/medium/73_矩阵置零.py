#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
from preImport import *
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row0, col0 = False, False # 第一行和第一列是否有0
        # 先標記第一行和第一列是否有0
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
                break
        # 用第一行和第一列來標記其他行列是否有0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 根據第一行和第一列的標記，將其他行列置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 最後根據row0和col0來決定第一行和第一列是否置零
        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0

# @lc code=end
sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
print(matrix)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
print(matrix)
