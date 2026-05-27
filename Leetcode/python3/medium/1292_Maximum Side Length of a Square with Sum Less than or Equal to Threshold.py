#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat, start=1):
            for j, x in enumerate(row, start=1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + x

        def query(r1: int, c1: int, r2: int, c2: int) -> int:
            return s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]

        ans = 0
        for i in range(m):
            for j in range(n):
                # for k in range(min(m - i, n - j)):
                # 可以直接從上次的結果開始，減少不必要的計算
                for k in range(ans, min(m - i, n - j)):
                    if query(i, j, i + k, j + k) <= threshold:
                        ans = max(ans, k + 1)
                    else:
                        break
        return ans
# @lc code=end

