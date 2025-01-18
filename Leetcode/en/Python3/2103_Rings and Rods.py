# @algorithm @lc id=2226 lang=python3 
# @title rings-and-rods


from en.Python3.mod.preImport import *
# @test("B0B6G0R6R0R6G9")=1
# @test("B0R0G0R9R0B0G0")=1
# @test("G4")=0
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) // 2
        cnt = [defaultdict(int) for _ in range(10)]
        for i in range(n):
            color, pos = rings[2*i], rings[2*i+1]
            cnt[int(pos)][color] += 1
        ans = 0
        for i in range(10):
            if cnt[i]['R'] > 0 and cnt[i]['G'] > 0 and cnt[i]['B'] > 0:
                ans += 1
        return ans