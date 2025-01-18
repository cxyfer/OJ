# @algorithm @lc id=3179 lang=python3 
# @title maximum-points-after-collecting-coins-from-all-nodes


from en.Python3.mod.preImport import *
# @test([[0,1],[1,2],[2,3]],[10,10,3,3],5)=11
# @test([[0,1],[0,2]],[8,4,4],0)=16
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        