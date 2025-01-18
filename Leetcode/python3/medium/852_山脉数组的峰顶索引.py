#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#
from preImport import *
# @lc code=start
class Solution:
    """
        Binary Search
        Time: O(logn)
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1
        while left <= right: # [left, right]
            mid = (left + right) // 2
            if arr[mid] > arr[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

