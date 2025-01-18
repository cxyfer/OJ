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
class Solution1:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(i, j): # 以 (i, j) 為右下角的最大正方形邊長
            if i < 0 or j < 0:
                return 0
            if matrix[i][j] == 0:
                return 0
            return 1 + min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1))
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
        return ans
    
class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        return sum(sum(row) for row in f)
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [[0,1,1,1],[1,1,1,1],[0,1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#

