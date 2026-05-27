#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        s = [[0] * (m + 1) for _ in range(n + 1)]
        for i, row in enumerate(matrix, 1):
            for j, val in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + val
        self.s = s

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2 + 1][c2 + 1] - self.s[r1][c2 + 1] - self.s[r2 + 1][c1] + self.s[r1][c1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

