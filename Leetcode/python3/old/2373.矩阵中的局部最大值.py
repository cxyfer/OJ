#
# @lc app=leetcode.cn id=2373 lang=python3
#
# [2373] 矩阵中的局部最大值
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n-2):
            for j in range(n-2):
                grid[i][j] = max( max(row[j:j+3]) for row in grid[i:i+3])
            grid[i].pop()
            grid[i].pop()
        grid.pop()
        grid.pop()
        return grid
# @lc code=end

