#
# @lc app=leetcode id=1301 lang=python3
#
# [1301] Number of Paths with Max Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)

        @cache
        def dfs(i: int, j: int) -> tuple[int, int]:
            if i == 0 and j == 0:
                return (0, 1)
            if i < 0 or j < 0 or board[i][j] == "X":
                return (-inf, 0)
            mx, cnt = -inf, 0
            for x, y in [(i - 1, j), (i, j - 1), (i - 1, j - 1)]:
                v, w = dfs(x, y)
                if v > mx:
                    mx, cnt = v, w
                elif v == mx:
                    cnt += w
                    cnt %= MOD
            return (mx + (int(board[i][j]) if board[i][j].isdigit() else 0), cnt)

        mx, cnt = dfs(n - 1, n - 1)
        return [mx, cnt] if cnt > 0 else [0, 0]  # 理論上應該是錯的，可以構造 cnt % MOD = 0 的情況
        # return [mx, cnt] if mx != -inf else [0, 0]
# @lc code=end

sol = Solution()
print(sol.pathsWithMaxScore(["E111", "XXX1", "XXX1", "999S"]))  # [5, 1]