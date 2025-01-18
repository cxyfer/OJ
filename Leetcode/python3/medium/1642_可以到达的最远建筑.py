#
# @lc app=leetcode.cn id=1642 lang=python3
#
# [1642] 可以到达的最远建筑
#
from preImport import *
# @lc code=start
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
# @lc code=end

