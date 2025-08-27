#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
DIR = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, d: int, turn: bool, tgt: int) -> int:
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != tgt:
                return 0
            res = dfs(i + DIR[d][0], j + DIR[d][1], d, turn, 2 - tgt)
            if not turn:
                nd = (d + 1) % 4
                res = max(res, dfs(i + DIR[nd][0], j + DIR[nd][1], nd, True, 2 - tgt))
            return res + 1
        
        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val != 1:
                    continue
                for d, (dx, dy) in enumerate(DIR):
                    ans = max(ans, dfs(i + dx, j + dy, d, False, 2) + 1)
        return ans
# @lc code=end

sol = Solution()
print(sol.lenOfVDiagonal([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])) # 5
