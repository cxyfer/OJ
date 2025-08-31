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
        def set(i, j, val):
            row[i] |= 1 << val
            col[j] |= 1 << val
            box[i // 3 * 3 + j // 3] |= 1 << val
        def unset(i, j, val):
            row[i] &= ~(1 << val)
            col[j] &= ~(1 << val)
            box[i // 3 * 3 + j // 3] &= ~(1 << val)
        for i, line in enumerate(board):
            for j, val in enumerate(line):
                if val != '.':
                    set(i, j, int(val) - 1)
        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)
            if board[i][j] != '.':
                return dfs(i, j + 1)
            # for k in range(9):
            #     if row[i] & (1 << k) or col[j] & (1 << k) or box[i // 3 * 3 + j // 3] & (1 << k):
            #         continue
            msk = (row[i] | col[j] | box[i // 3 * 3 + j // 3]) ^ ((1 << 9) - 1)
            while msk:
                k = (msk & -msk).bit_length() - 1
                set(i, j, k)
                board[i][j] = str(k + 1)
                if dfs(i, j + 1):
                    return True
                unset(i, j, k)
                board[i][j] = '.'
                msk &= (msk - 1)
            return False
        dfs(0, 0)
# @lc code=end

