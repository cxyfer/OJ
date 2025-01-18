#
# @lc app=leetcode.cn id=2660 lang=python3
#
# [2660] 保龄球游戏的获胜者
#
from preImport import *
# @lc code=start
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def f(player: List[int]) -> int:
            res = 0
            pre1 = pre2 = 0
            for x in player:
                res += x * 2 if pre1 or pre2 else x
                pre1, pre2 = pre2, x == 10
            return res
        return 1 if f(player1) > f(player2) else 2 if f(player1) < f(player2) else 0
# @lc code=end

