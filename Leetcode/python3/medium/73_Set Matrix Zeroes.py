#
# @lc app=leetcode id=73 lang=python3
# @lcpr version=30201
#
# [73] Set Matrix Zeroes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. 使用額外 O(n) 空間標記。
            使用兩個陣列 row 和 col 來標記原陣列的行和列是否包含 0
        2. 使用原陣列的第一直行和第一橫列作為標記。
            但由於標記會破壞原本的數據，所以需要另外使用兩個變量來標記原本的第一直行和第一橫列是否包含 0
            置 0 時先忽略第一直行和第一橫列，從第二直行和第二橫列開始，最後再根據兩個變量來處理第一直行和第一橫列
        3. 從 2. 進一步優化，同樣使用原陣列的第一直行和第一橫列作為標記，但可以只使用一個額外變數來標記原本的第一直行是否包含 0
            將原陣列的第一橫列是否包含 0 的標記放在 matrix[0][0] 中，如此就只需要標記原本的第一直行是否包含 0
            標記時從 每一橫列 的 第二直行 開始，
            由於會用到第一橫列的資訊，置零時先忽略第一橫列，從第二橫列開始
            同樣地，由於會用到第一直行的資訊，在置零每一橫列時，將第一直行留在該橫列的最後處理。
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # return self.solve1(matrix)
        # return self.solve2(matrix)
        return self.solve3(matrix)
    def solve1(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
    def solve2(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        col0 = any(matrix[i][0] == 0 for i in range(m)) # 原陣列的第一行是否有 0 
        row0 = any(matrix[0][j] == 0 for j in range(n)) # 原陣列的第一列是否有 0  
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0: 
                    matrix[i][0] = matrix[0][j] = 0 # 用原陣列的第一行和第一列作為標記
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0
        if row0:
            for j in range(n):
                matrix[0][j] = 0
    def solve3(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        col0 = False # 第一直行是否有 0
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m): # 從第二橫列開始置零，原本的第一橫列保留到最後處理
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0
        if matrix[0][0] == 0: # /置零第一橫列
            for j in range(1, n):
                matrix[0][j] = 0
        if col0:
            matrix[0][0] = 0
# @lc code=end

sol = Solution()
sol.setZeroes([[1],[0]])

#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

