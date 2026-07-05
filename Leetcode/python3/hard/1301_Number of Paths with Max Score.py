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
        # return [mx, cnt] if cnt > 0 else [0, 0]  # 當 cnt % MOD == 0 時，會判斷錯誤
        return [mx, cnt] if mx != -inf else [0, 0]
# @lc code=end

sol = Solution()
print(sol.pathsWithMaxScore(["E111", "XXX1", "XXX1", "999S"]))  # [5, 1]


def hack():
    B = MOD.bit_length()
    n = 3 * B + 1
    grid = [["X"] * n for _ in range(n)]

    for i in range(n):
        grid[i][n - 1] = "1"
    
    for b in range(B):
        r, c = 3 * b, b
        for i in range(r, r + 4):
            grid[i][c] = "1"
        for i in range(r + 2, r + 4):
            grid[i][c + 1] = "1"
        if (MOD >> b) & 1:
            for j in range(c, n):
                grid[r][j] = "1"

    grid[0][0] = "E"
    grid[n - 1][n - 1] = "S"

    board = ["".join(row) for row in grid]
    # import os
    # import json
    # os.makedirs("hacks", exist_ok=True)
    # with open("hacks/hack_1301.txt", "w") as f:
    #     f.write(json.dumps(board))
    return board


print(sol.pathsWithMaxScore(hack()))  # [179, 0]
