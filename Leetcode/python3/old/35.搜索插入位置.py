#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from mod.preImport import *
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid
            else: left = mid + 1
        return right
         # 根據區間 [left, right) ， 考慮4種情況
            # 1. target在nums中，return middle
            # 2. target不在nums中，且target比nums中所有數都小，此時right最終為0，return right
            # 3. target不在nums中，且target比nums中所有數都大，此時right最終為n，return right
            # 4. target不在nums中，且target在nums中間，return right
# @lc code=end

