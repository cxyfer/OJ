#
# @lc app=leetcode id=419 lang=python3
# @lcpr version=30203
#
# [419] Battleships in a Board
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == '.':
                    continue
                if (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.') :
                    ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["."]]\n
# @lcpr case=end

#

