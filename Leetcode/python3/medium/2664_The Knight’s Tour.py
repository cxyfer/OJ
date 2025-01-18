#
# @lc app=leetcode id=2664 lang=python3
# @lcpr version=30204
#
# [2664] The Knight’s Tour
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        ans[r][c] = 0

        def dfs(x: int, y: int, step: int) -> bool:
            if step == m * n:
                return True
            for dx, dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = step
                    if dfs(nx, ny, step + 1):
                        return True
                    ans[nx][ny] = -1
            return False
        dfs(r, c, 1)
        return ans
# @lc code=end



#
# @lcpr case=start
# 1\n1\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# 3\n4\n0\n0\n
# @lcpr case=end

#

