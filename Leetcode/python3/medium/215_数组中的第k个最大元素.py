#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from preImport import *
# @lc code=start
class Solution:
    """
        heapq實現的是min heap，所以要找第k大的元素，就要維護一個size為k的min heap
        Time: O(n + klogn)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k:
                heapq.heappop(hp)
        return hp[0] # hp[0] is the smallest element in the heap
# @lc code=end

