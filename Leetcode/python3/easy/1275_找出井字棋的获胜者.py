#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#
from preImport import *
# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        mp = [[0] * 3 for _ in range(3)]
        def check():
            for i in range(3):
                if mp[i][0] == mp[i][1] == mp[i][2] and mp[i][0] != 0:
                    return mp[i][0]
                if mp[0][i] == mp[1][i] == mp[2][i] and mp[0][i] != 0:
                    return mp[0][i]
            if mp[0][0] == mp[1][1] == mp[2][2] and mp[0][0] != 0:
                return mp[0][0]
            if mp[0][2] == mp[1][1] == mp[2][0] and mp[0][2] != 0:
                return mp[0][2]
            return 0 # no winner
        for i, (x, y) in enumerate(moves):
            mp[x][y] = 1 if i % 2 == 0 else -1
            if i < 4: # no winner
                continue
            res = check()
            if res != 0:
                return "A" if res == 1 else "B"
        return "Draw" if len(moves) == 9 else "Pending"# @lc code=end

