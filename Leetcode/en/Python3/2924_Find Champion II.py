# @algorithm @lc id=3189 lang=python3 
# @title find-champion-ii


from en.Python3.mod.preImport import *
# @test(3,[[0,1],[1,2]])=0
# @test(4,[[0,2],[1,3],[1,2]])=-1
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for u, v in edges:
            indeg[v] += 1
        ans = -1
        for i in range(n):
            if indeg[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans
        