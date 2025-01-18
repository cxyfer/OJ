#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        heapq實現的是min heap，所以要找第k大的元素，就要維護一個size為k的min heap
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
# @lc code=end

