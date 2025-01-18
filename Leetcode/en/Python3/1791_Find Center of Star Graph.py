# @algorithm @lc id=1916 lang=python3 
# @title find-center-of-star-graph


from en.Python3.mod.preImport import *
# @test([[1,2],[2,3],[4,2]])=2
# @test([[1,2],[5,1],[1,3],[1,4]])=1
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        