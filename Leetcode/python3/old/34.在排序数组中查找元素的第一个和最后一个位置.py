#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from mod.preImport import *
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def findLeft():
            left, right = 0, n-1
            while left <= right:
                middle = left + (right-left)//2
                if nums[middle] < target: # [middle+1, right]
                    left = middle + 1
                elif nums[middle] > target: # [left, middle-1]
                    right = middle - 1
                else: # 繼續往左找最左邊的
                    right = middle - 1
            if left < 0 or left >= n:
               return -1
            return left if nums[left] == target else -1
        def findRight():
            left, right = 0, n-1
            while left <= right:
                middle = left + (right-left)//2
                if nums[middle] < target: # [middle+1, right]
                    left = middle + 1
                elif nums[middle] > target: # [left, middle-1]
                    right = middle - 1
                else: # 繼續往右找最右邊的
                    left = middle + 1
            if right < 0 or right >= n:
                return -1
            return right if nums[right] == target else -1
        
        return [findLeft(), findRight()]
# @lc code=end

