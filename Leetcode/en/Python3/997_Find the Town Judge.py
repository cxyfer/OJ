# @algorithm @lc id=1039 lang=python3 
# @title find-the-town-judge


from en.Python3.mod.preImport import *
# @test(2,[[1,2]])=2
# @test(3,[[1,3],[2,3]])=3
# @test(3,[[1,3],[2,3],[3,1]])=-1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0] * (n + 1)
        outdeg = [0] * (n + 1)
        for a, b in trust:
            indeg[b] += 1
            outdeg[a] += 1
        for i in range(1, n + 1):
            if indeg[i] == n - 1 and outdeg[i] == 0:
                return i
        return -1