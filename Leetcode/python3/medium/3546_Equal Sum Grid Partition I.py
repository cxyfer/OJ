#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        # 二維前綴和
        s = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i - 1][j - 1]
        if s[n][m] & 1:
            return False
        for i in range(1, n + 1):
            if s[i][m] == s[n][m] // 2:
                return True
        for j in range(1, m + 1):
            if s[n][j] == s[n][m] // 2:
                return True
        return False
# @lc code=end

