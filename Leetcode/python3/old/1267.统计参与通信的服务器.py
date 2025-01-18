#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#
from mod.preImport import *
# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Use Counter() to replace List to save memory ?
        m, n = len(grid), len(grid[0])
        # row, col = [0]*m, [0]*n
        row, col = Counter(), Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    ans += 1
        return ans
# @lc code=end

