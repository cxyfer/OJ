#
# @lc app=leetcode id=289 lang=python3
# @lcpr version=30201
#
# [289] Game of Life
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # return self.solve1(board)
        return self.solve2(board)
    """
        1. 使用額外空間
    """
    def solve1(self, board: List[List[int]]) -> None:
        r, c = len(board), len(board[0])
        tmp = [[board[i][j] for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                live = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < r and 0 <= y < c and (x != i or y != j):
                            live += tmp[x][y]
                if tmp[i][j] == 1:
                    if live < 2 or live > 3: # 1 -> 0
                        board[i][j] = 0
                else:
                    if live == 3: # 0 -> 1
                        board[i][j] = 1
    """
        2. 使用額外狀態，但是不使用額外空間
        用最後2bit表示當前狀態和下一時刻狀態，最低位表示當前狀態，倒數第二位表示下一時刻狀態
        而 0 為死， 1 為活，故 00 表示死，01 表示活變死，10 表示死變活，11 表示活
        由於第二位初始就是 0 ，所以只要判斷下一時刻狀態為活的情況即可
    """
    def solve2(self, board: List[List[int]]) -> None:
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                live = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < r and 0 <= y < c and (x != i or y != j):
                            live += board[x][y] & 1
                if board[i][j] & 1:
                    if live == 2 or live == 3: # 活細胞保持活
                        board[i][j] += 2
                else:
                    if live == 3: # 死細胞變活
                        board[i][j] += 2
        for i in range(r):
            for j in range(c):
                board[i][j] >>= 1 # 更新狀態
# @lc code=end



#
# @lcpr case=start
# [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

#

