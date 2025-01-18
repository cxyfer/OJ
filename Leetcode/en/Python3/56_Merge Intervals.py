# @algorithm @lc id=56 lang=python3 
# @title merge-intervals


from en.Python3.mod.preImport import *
# @test([[1,3],[2,6],[8,10],[15,18]])=[[1,6],[8,10],[15,18]]
# @test([[1,4],[4,5]])=[[1,5]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not ans or x > ans[-1][1]: # not overlap
                ans.append([x, y])
            else:
                ans[-1][1] = max(ans[-1][1], y) # overlap, update interval
        return ans