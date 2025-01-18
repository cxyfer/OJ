#
# @lc app=leetcode.cn id=2482 lang=python3
#
# [2482] 行和列中一和零的差值
#
from preImport import *
# @lc code=start
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # diff[i][j] = rows[i] + cols[j] - (n - rows[i]) - (m - cols[j])
                diff[i][j] = 2 * rows[i] + 2 * cols[j] - m - n
        return diff
# @lc code=end

