#
# @lc app=leetcode.cn id=2940 lang=python3
#
# [2940] 找到 Alice 和 Bob 可以相遇的建筑
#
from preImport import *
# @lc code=start
class Solution:
    """
        離線：Min Heap / Monotonic Stack
        在線：ST表二分 / 樹狀樹組二分 / 線段樹二分
    """
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        return self.solveByHeap(heights, queries)
    """
        1. 離線 + Min Heap
    """
    def solveByHeap(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        # 依照 j 來處理
        left = defaultdict(list)
        for q_idx, (i, j) in enumerate(queries):
            # 保證 i <= j
            if i > j:
                i, j = j, i
            
            # 可以從 i 直接跳到 j ， 直接回答
            if i == j or heights[i] < heights[j]:
                ans[q_idx] = j
            else:
                left[j].append((heights[i], q_idx)) # 離線
        hp = [] # min heap
        for j, h_j in enumerate(heights):
            # 若堆頂元素的高度 hp[0][0](h_i) < h_j ，可以跳到 j，即該詢問答案為 j
            while hp and hp[0][0] < h_j:
                q_idx = heappop(hp)[1]
                ans[q_idx] = j # 回答
            # 將 left[j] 中的詢問加入堆中
            for p in left[j]:
                heappush(hp, p)
        return ans
    """
        2. 在線 + 線段樹
    """
    def solveBySegmentTree(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        pass
# @lc code=end

