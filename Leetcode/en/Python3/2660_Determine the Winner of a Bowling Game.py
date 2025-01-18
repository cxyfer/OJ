# @algorithm @lc id=2684 lang=python3 
# @title determine-the-winner-of-a-bowling-game


from en.Python3.mod.preImport import *
# @test([4,10,7,9],[6,5,2,3])=1
# @test([3,5,7,6],[8,10,10,2])=2
# @test([2,3],[4,1])=0
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
        