#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from preImport import *
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        return self.solve2(nums)
    """
        2. Binary Search
        一段遞增，或兩段遞增
        - 紅：在最小值左側
        - 藍：最小值本身或在最小值右側
    """
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-2 # [left, right] 由於 nums[n-1] 一定是藍色，所以右界為 n-2
        while left <= right: # 區間不為空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]: # 藍色：不管是一段遞增還是兩段遞增，最小值是 mid 或在 mid 的左側，故 mid 不是最小值本身就是在最小值右側
                right = mid - 1
            else: # 紅色：只可能是兩段遞增，最小值一定在 mid 的右側，故 mid 在最小值左側
                left = mid + 1
        return nums[left]
# @lc code=end
sol = Solution()
print(sol.findMin([3,4,5,1,2])) # 1
print(sol.findMin([4,5,6,7,0,1,2])) # 0
print(sol.findMin([11,13,15,17])) # 11