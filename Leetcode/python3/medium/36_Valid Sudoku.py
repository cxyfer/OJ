#
# @lc app=leetcode id=36 lang=python3
# @lcpr version=30204
#
# [36] Valid Sudoku
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = [0] * 9, [0] * 9, [0] * 9
        for i, line in enumerate(board):
            for j, ch in enumerate(line):
                if ch == ".":
                    continue
                x = 1 << (ord(ch) - ord("1"))
                if row[i] & x or col[j] & x or box[i // 3 * 3 + j // 3] & x:
                    return False
                row[i] |= x
                col[j] |= x
                box[i // 3 * 3 + j // 3] |= x
        return True
# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

