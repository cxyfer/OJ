# @algorithm @lc id=57 lang=python3 
# @title insert-interval


from en.Python3.mod.preImport import *
# @test([[1,3],[6,9]],[2,5])=[[1,5],[6,9]]
# @test([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])=[[1,2],[3,10],[12,16]]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        # 1. Greedy
        # Smilar to 56. Merge Intervals
        # Time: O(nlogn) # sort
        """
        ans = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not ans or x > ans[-1][1]: # not overlap
                ans.append([x, y])
            else:
                ans[-1][1] = max(ans[-1][1], y) # overlap, update interval
        return ans