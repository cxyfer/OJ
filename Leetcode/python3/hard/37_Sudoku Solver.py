#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col, box = [0] * 9, [0] * 9, [0] * 9
        for i, line in enumerate(board):
            for j, val in enumerate(line):
                if val != '.':
                    row[i] |= 1 << int(val)
                    col[j] |= 1 << int(val)
                    box[i // 3 * 3 + j // 3] |= 1 << int(val)
        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)
            if board[i][j] != '.':
                return dfs(i, j + 1)
            for k in range(1, 10):
                if row[i] & (1 << k) or col[j] & (1 << k) or box[i // 3 * 3 + j // 3] & (1 << k):
                    continue
                row[i] |= (1 << k)
                col[j] |= (1 << k)
                box[i // 3 * 3 + j // 3] |= (1 << k)
                board[i][j] = str(k)
                if dfs(i, j + 1):
                    return True
                row[i] &= ~(1 << k)
                col[j] &= ~(1 << k)
                box[i // 3 * 3 + j // 3] &= ~(1 << k)
                board[i][j] = '.'
            return False
        dfs(0, 0)
# @lc code=end

