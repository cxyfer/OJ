# @algorithm @lc id=2149 lang=python3 
# @title remove-colored-pieces-if-both-neighbors-are-the-same-color


from en.Python3.mod.preImport import *
# @test("AAABABB")=true
# @test("AA")=false
# @test("ABBBBBBBAAA")=false
class Solution:
    """
        因為要有連續三個相同的顏色才能刪除，故刪除A不會影響到B，反之亦然
        所以只要計算連續3個相同顏色的數量，再比較A和B的數量即可
    """
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        cntA, cntB = 0, 0
        for i in range(1, n-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    cntA += 1
                else:
                    cntB += 1
        return cntA > cntB