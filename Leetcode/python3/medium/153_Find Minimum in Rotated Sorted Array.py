#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lcpr-template-start
from preImport import *


# @lcpr-template-end
"""
由於在旋轉後會形成一段或兩段遞增的數列，且本題保證元素皆不相同，
我們可以利用 nums[x] 與最後一個元素的比較來判斷最小值在 x 的左側還是右側。
- nums[x] <= nums[-1]：最小值在 x 的左側或 x 是最小值本身
- nums[x] > nums[-1]：最小值在 x 的右側

類題：
- 154. Find Minimum in Rotated Sorted Array II (元素可重複)
"""
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
