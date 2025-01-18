# @algorithm @lc id=37 lang=python3 
# @title sudoku-solver


from en.Python3.mod.preImport import *
# @test([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])=[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
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
        