#
# @lc app=leetcode id=1958 lang=python3
# @lcpr version=30204
#
# [1958] Check if Move is Legal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def check(dx, dy):
            x, y = rMove + dx, cMove + dy
            cnt = 0 # 中間點的數量
            while 0 <= x < 8 and 0 <= y < 8: 
                if board[x][y] == color: # 找到另外一個端點
                    return True if cnt > 0 else False
                if board[x][y] == ".": # 中間不連續
                    return False
                x += dx
                y += dy
                cnt += 1
            return False
        # 檢查 8 個方向
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if check(dx, dy):
                    return True
        return False
# @lc code=end




#
# @lcpr case=start
# [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]\n4\n3\n"B"\n
# @lcpr case=end

# @lcpr case=start
# [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]\n4\n4\n"W"\n
# @lcpr case=end

#

