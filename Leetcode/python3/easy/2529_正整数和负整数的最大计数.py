#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#
from preImport import *
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def find_left(nums: List[int], target: int) -> int: # find the leftmost target
            n = len(nums)
            left, right = 0, n - 1 # [left, right]
            while left <= right: # 區間不為空
                # mid = left + (right - left) // 2
                mid = (left + right) // 2 
                if nums[mid] < target: # [mid+1, right]
                    left = mid + 1 
                else: # [left, mid-1]
                    right = mid - 1
            return left # or right+1
        neg = find_left(nums, 0)
        pos = len(nums) - find_left(nums, 1)
        return max(neg, pos)
# @lc code=end
sol = Solution()
print(sol.maximumCount([-3,-2,-1,0,0,1,2])) # 3
