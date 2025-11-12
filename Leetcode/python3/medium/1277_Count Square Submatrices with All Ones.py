#
# @lc app=leetcode id=1277 lang=python3
# @lcpr version=30204
#
# [1277] Count Square Submatrices with All Ones
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        f = [[0] * m for _ in range(n)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 1:
                    if i > 0 and j > 0:
                        f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                    else:
                        f[i][j] = 1
        return sum(sum(row) for row in f)
# @lc code=end



#
# @lcpr case=start
# [[0,1,1,1],[1,1,1,1],[0,1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#

