#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
from array import array

class Solution1a:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        s = [[array('i', [0] * 2) for _ in range(n + 1)] for _ in range(m + 1)]
        for i, row in enumerate(grid, start=1):
            for j, ch in enumerate(row, start=1):
                for b in range(2):
                    s[i][j][b] = s[i - 1][j][b] + s[i][j - 1][b] - s[i - 1][j - 1][b] + (ord(ch) - ord('X') == b)
                if s[i][j][0] == s[i][j][1] > 0:
                    ans += 1
        return ans

class Solution1b:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        ans = 0
        f, nf = [[0] * 2 for _ in range(n + 1)], [[0] * 2 for _ in range(n + 1)]
        for row in grid:
            for j, ch in enumerate(row, start=1):
                for b in range(2):
                    nf[j][b] = f[j][b] + nf[j - 1][b] - f[j - 1][b] + (ord(ch) - ord('X') == b)
                if nf[j][0] == nf[j][1] > 0:
                    ans += 1
            f, nf = nf, f
        return ans

class Solution2:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        ans = 0
        col = [[0, 0] for _ in range(n)]
        for row in grid:
            cnt = [0, 0]
            for j, ch in enumerate(row):
                if ch != '.':
                    col[j][ord(ch) - ord('X')] += 1
                for b in range(2):
                    cnt[b] += col[j][b]
                if cnt[0] == cnt[1] > 0:
                    ans += 1
        return ans

# Solution = Solution1a
# Solution = Solution1b
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))