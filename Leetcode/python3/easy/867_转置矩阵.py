#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
from preImport import *
# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [ [0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[j][i]
        return ans
# @lc code=end

