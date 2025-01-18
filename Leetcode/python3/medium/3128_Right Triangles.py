#
# @lc app=leetcode id=3128 lang=python3
# @lcpr version=30204
#
# [3128] Right Triangles
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_cnt = [0] * m
        col_cnt = [0] * n
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    ans += (row_cnt[i] - 1) * (col_cnt[j] - 1)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,1,0],[0,1,1],[0,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,1,0,1],[1,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[1,0,0],[1,0,0]]\n
# @lcpr case=end

#

