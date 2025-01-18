# @algorithm @lc id=3398 lang=python3 
# @title make-a-square-with-the-same-color


from en.Python3.mod.preImport import *
# @test([["B","W","B"],["B","W","W"],["B","W","B"]])=true
# @test([["B","W","B"],["W","B","W"],["B","W","B"]])=false
# @test([["B","W","B"],["B","W","W"],["B","W","W"]])=true
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                cnt = Counter()
                for a in range(2):
                    for b in range(2):
                        cnt[grid[i+a][j+b]] += 1
                if cnt['B'] >= 3 or cnt['W'] >= 3:
                    return True
        return False