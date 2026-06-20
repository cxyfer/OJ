#
# @lc app=leetcode id=3963 lang=python3
#
# [3963] Create Grid With Exactly One Path
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n for _ in range(m)]
        for i in range(m):
            grid[i][0] = "."
        for j in range(n):
            grid[m - 1][j] = "."
        return ["".join(row) for row in grid]
# @lc code=end

