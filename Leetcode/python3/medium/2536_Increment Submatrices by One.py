#
# @lc app=leetcode id=2536 lang=python3
#
# [2536] Increment Submatrices by One
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            # 1-based indexing
            diff[r1 + 1][c1 + 1] += 1
            diff[r1 + 1][c2 + 2] -= 1
            diff[r2 + 2][c1 + 1] -= 1
            diff[r2 + 2][c2 + 2] += 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
        return list(map(lambda row: row[1:-1], diff[1:-1]))
# @lc code=end

sol = Solution()
print(sol.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]))