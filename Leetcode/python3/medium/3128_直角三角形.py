#
# @lc app=leetcode.cn id=3128 lang=python3
#
# [3128] 直角三角形
#
from preImport import *
# @lc code=start
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        col_sum = [-1] * m # 提前減一
        for i in range(n):
            for j in range(m):
                col_sum[j] += grid[i][j]
        ans = 0
        for row in grid:
            row_sum = sum(row) - 1
            ans += row_sum * sum(c for x, c in zip(row, col_sum) if x)
        return ans

# @lc code=end
sol = Solution()
print(sol.numberOfRightTriangles([[0,1,0],[0,1,1],[0,1,0]])) # 2
print(sol.numberOfRightTriangles([[1,0,0,0],[0,1,0,1],[1,0,0,0]])) # 0
print(sol.numberOfRightTriangles([[1,0,1],[1,0,0],[1,0,0]])) # 2