#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from mod.preImport import *
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid
            else: left = mid + 1
        return -1
# @lc code=end

