# @algorithm @lc id=1762 lang=python3 
# @title furthest-building-you-can-reach


from en.Python3.mod.preImport import *
# @test([4,2,7,6,9,14,12],5,1)=4
# @test([4,12,2,7,3,18,20,3,19],10,2)=7
# @test([14,3,19,3],17,0)=3
class Solution:
    """
        Greedy + Heap
        用 Min Heap 維護需要使用 ladder 的 delta_h
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        hp = [] # min heap
        sum_h = 0 # sum of bricks
        for i in range(1, n):
            d = heights[i] - heights[i - 1] # delta_h
            if d > 0:
                heappush(hp, d)
                if len(hp) > ladders: # 最小的 delta_h 不用 ladder，改用 brick 代替
                    sum_h += heappop(hp)
                if sum_h > bricks: # bricks 不夠用
                    return i - 1
        return n - 1 # 可到達最後一個建築