#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lcpr-template-start
from preImport import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        n = len(nums)

        """
        T: 最小值在 mid 的左側或 mid 是最小值本身
        F: 最小值在 mid 的右側
        """
        def check(mid: int) -> bool:
            return nums[mid] <= nums[-1]

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):  # 最小值是 mid 或在 mid 的左側
                right = mid - 1
            else:  # 只可能是兩段遞增，最小值一定在 mid 的右側
                left = mid + 1
        return nums[left]
# @lc code=end

sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))  # 1
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
print(sol.findMin([11, 13, 15, 17]))  # 11
