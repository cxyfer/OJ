#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#
from preImport import *
# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        left, right = 0, n-1
        for i in range(n):
            ans += mat[i][left] + mat[i][right]
            left += 1
            right -= 1
        if n % 2 == 1:
            ans -= mat[n//2][n//2]
        return ans
# @lc code=end

