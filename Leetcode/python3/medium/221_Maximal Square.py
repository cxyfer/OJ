#
# @lc app=leetcode id=221 lang=python3
# @lcpr version=30204
#
# [221] Maximal Square
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if matrix[i][j] == "0":
                return 0
            return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans ** 2
# @lc code=end



#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#

