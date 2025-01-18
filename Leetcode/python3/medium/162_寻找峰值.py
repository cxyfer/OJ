#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
from preImport import *
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return self.solve11(nums)
        return self.solve2(nums)
        # return self.solve3(nums)
    """
        1. Simple Linear Search
    """
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [float('-inf')] + nums + [float('-inf')]
        for i in range(1, n+1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1
        return -1
    def solve11(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if x > nums[ans]:
                ans = i
        return ans
    """
        2. Binary Search
    """
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        # left, right = 0, n-1 # [left, right]
        left, right = 0, n-2 # [left, right] 右界為 n-2
        while(left <= right): # 區間不為空
            mid = (left + right) // 2
            # if mid == (n-1) or nums[mid] > nums[mid+1]: # 若 mid 已經是最後一個元素，則不用比較
            if nums[mid] > nums[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
    def solve3(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while (left <= right):
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif (mid > 0 and nums[mid-1] > nums[mid]):
                right = mid -1
            else:
                left = mid + 1
        return None
# @lc code=end

sol = Solution()
print(sol.findPeakElement([1]))
print(sol.findPeakElement([1,2,3,1])) # 2
print(sol.findPeakElement([1,2,1,3,5,6,4])) # 5