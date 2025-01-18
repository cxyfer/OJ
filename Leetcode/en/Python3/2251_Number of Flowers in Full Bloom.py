# @algorithm @lc id=2334 lang=python3 
# @title number-of-flowers-in-full-bloom


from en.Python3.mod.preImport import *
# @test([[1,6],[3,7],[9,12],[4,13]],[2,3,7,11])=[1,2,2,2]
# @test([[1,10],[3,3]],[3,3,2])=[2,2,1]
class Solution:
    """
        Binary Search
    """
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]

