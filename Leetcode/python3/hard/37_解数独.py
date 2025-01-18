#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
from preImport import *
# @lc code=start
class Solution:
    """
        Backtracking
    """
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board, row, col):
            if col == 9:
                return backtrack(board, row+1, 0)
            if row == 9:
                return True
            for i in range(row, 9):
                for j in range(col, 9):
                    if board[i][j] != '.':
                        return backtrack(board, i, j+1)
                    for ch in range(1, 10):
                        if not isValid(i, j, str(ch)):
                            continue
                        board[i][j] = str(ch)
                        if backtrack(board, i, j+1):
                            return True
                        board[i][j] = '.' # 回溯
                    return False
            return False
        def isValid(row, col, ch):
            for i in range(9):
                if board[row][i] == ch:
                    return False
                if board[i][col] == ch:
                    return False
                if board[(row//3)*3 + i//3][(col//3)*3 + i%3] == ch:
                    return False
            return True
        
        backtrack(board, 0, 0)
        return
# @lc code=end

