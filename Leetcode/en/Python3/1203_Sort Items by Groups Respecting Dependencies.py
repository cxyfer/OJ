# @algorithm @lc id=1309 lang=python3 
# @title sort-items-by-groups-respecting-dependencies


from en.Python3.mod.preImport import *
# @test(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3,6],[],[],[]])=[6,3,4,1,5,2,0,7]
# @test(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3],[],[4],[]])=[]
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        