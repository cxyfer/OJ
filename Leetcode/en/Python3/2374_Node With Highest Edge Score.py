# @algorithm @lc id=2455 lang=python3 
# @title node-with-highest-edge-score


from en.Python3.mod.preImport import *
# @test([1,0,0,0,0,7,7,5])=7
# @test([2,0,0,2])=0
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i, to in enumerate(edges):
            scores[to] += i
        ans = 0
        for i, s in enumerate(scores):
            if s > scores[ans]:
                ans = i
        return ans
        