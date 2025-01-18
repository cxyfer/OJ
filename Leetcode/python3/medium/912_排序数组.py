#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from preImport import *
# @lc code=start
class Solution:
    """
        Heap sort
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hp = [-val for val in nums]
        heapq.heapify(hp) # O(n)
        ans = [-1] * n
        last = n - 1
        while hp:
            ans[last] = -heapq.heappop(hp)
            last -= 1
        return ans
# @lc code=end

