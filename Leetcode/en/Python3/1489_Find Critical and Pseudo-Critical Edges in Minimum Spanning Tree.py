# @algorithm @lc id=1613 lang=python3 
# @title find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree


from en.Python3.mod.preImport import *
# @test(5,[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])=[[0,1],[2,3,4,5]]
# @test(4,[[0,1,1],[1,2,1],[2,3,1],[0,3,1]])=[[],[0,1,2,3]]
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        