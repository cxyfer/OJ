#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#
from preImport import *
# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans
# @lc code=end

