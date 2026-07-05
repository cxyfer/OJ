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
        def dfs(i: int, j: int) -> tuple[int, int, bool]:
            if i == 0 and j == 0:
                return (0, 1, True)
            if i < 0 or j < 0 or board[i][j] == "X":
                return (0, 0, False)
            mx, cnt = 0, 0
            is_path = False
            for x, y in [(i - 1, j), (i, j - 1), (i - 1, j - 1)]:
                score, ways, flag = dfs(x, y)
                if score > mx:
                    mx, cnt, is_path = score, ways, flag
                elif score == mx:
                    cnt += ways
                    cnt %= MOD
                    is_path |= flag
            return (mx + (int(board[i][j]) if board[i][j].isdigit() else 0), cnt % MOD, is_path)
        
        mx, cnt, is_path = dfs(n - 1, n - 1)
        return [mx, cnt] if is_path else [0, 0]
# @lc code=end

