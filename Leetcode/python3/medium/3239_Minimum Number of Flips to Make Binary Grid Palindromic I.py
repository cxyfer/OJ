#
# @lc app=leetcode id=3239 lang=python3
# @lcpr version=30204
#
# [3239] Minimum Number of Flips to Make Binary Grid Palindromic I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans1 = ans2 = 0
        for i in range(n):
            for j in range(m // 2):
                if grid[i][j] != grid[i][m - j - 1]:
                    ans1 += 1
        for j in range(m):
            for i in range(n // 2):
                if grid[i][j] != grid[n - i - 1][j]:
                    ans2 += 1
        return min(ans1, ans2)
# @lc code=end



#
# @lcpr case=start
# [[1,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n
# @lcpr case=end

#

