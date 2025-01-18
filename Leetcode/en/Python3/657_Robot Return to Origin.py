# @algorithm @lc id=657 lang=python3 
# @title robot-return-to-origin


from en.Python3.mod.preImport import *
# @test("UD")=true
# @test("LL")=false
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt["U"] == cnt["D"] and cnt["L"] == cnt["R"]
        