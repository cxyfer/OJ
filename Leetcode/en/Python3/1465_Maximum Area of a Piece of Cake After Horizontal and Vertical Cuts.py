# @algorithm @lc id=1575 lang=python3 
# @title maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts


from en.Python3.mod.preImport import *
# @test(5,4,[1,2,4],[1,3])=4
# @test(5,4,[3,1],[1])=6
# @test(5,4,[3],[3])=9
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        h_cuts = [0] + sorted(horizontalCuts) + [h]
        w_cuts = [0] + sorted(verticalCuts) + [w]
        h_max = max(h_cuts[i] - h_cuts[i-1] for i in range(1, len(h_cuts)))
        w_max = max(w_cuts[i] - w_cuts[i-1] for i in range(1, len(w_cuts)))
        return h_max * w_max % MOD