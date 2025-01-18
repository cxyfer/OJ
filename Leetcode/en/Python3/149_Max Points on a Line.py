# @algorithm @lc id=149 lang=python3 
# @title max-points-on-a-line


from en.Python3.mod.preImport import *
# @test([[1,1],[2,2],[3,3]])=3
# @test([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])=4
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        