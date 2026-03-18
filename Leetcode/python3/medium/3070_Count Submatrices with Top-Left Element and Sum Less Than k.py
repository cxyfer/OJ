#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid, start=1):
            for j, val in enumerate(row, start=1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + val
                if s[i][j] <= k:
                    ans += 1
        return ans

class Solution2:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])
        ans = 0
        f, nf = [0] * (n + 1), [0] * (n + 1)
        for row in grid:
            for j, val in enumerate(row, start=1):
                nf[j] = f[j] + nf[j - 1] - f[j - 1] + val
                if nf[j] <= k:
                    ans += 1
            f, nf = nf, f
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

