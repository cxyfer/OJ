#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        s = [[0] * (m + 1) for _ in range(n + 1)]
        for i, row in enumerate(mat, 1):
            for j, val in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + val

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(n - 1, i + k), min(m - 1, j + k)
                ans[i][j] = s[r2 + 1][c2 + 1] - s[r1][c2 + 1] - s[r2 + 1][c1] + s[r1][c1]
        return ans
# @lc code=end

