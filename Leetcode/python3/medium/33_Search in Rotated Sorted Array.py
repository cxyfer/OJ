#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
# @lc code=start
"""
1. 兩次二分查找
基於 153. Find Minimum in Rotated Sorted Array 找到最小值的位置。
- F: 最小值在 mid 的右側
- T: 最小值在 mid 的左側或 mid 是最小值本身

再根據 target 和 nums[-1] 的大小關係，確定 target 在左段還是右段，再進行二分查找
"""


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def check(mid: int) -> bool:
            return nums[mid] <= nums[-1]

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):  # 最小值是 mid 或在 mid 的左側
                right = mid - 1
            else:  # 只可能是兩段遞增，最小值一定在 mid 的右側
                left = mid + 1
        return left

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 153. Find Minimum in Rotated Sorted Array
        # i = bisect_left(range(n), True, key=lambda x: nums[x] <= nums[-1])
        i = self.findMin(nums)  # min index

        left, right = (0, i) if target > nums[-1] else (i, n)  # [lo, hi)
        idx = bisect_left(nums, target, left, right)
        return idx if idx < n and nums[idx] == target else -1


"""
2. 一次二分查找
分類討論，基於 153 的思路：
- F: 最小值在 mid 的右側 => nums[mid] 在 兩段遞增的左段
- T: 最小值在 mid 的左側或 mid 是最小值本身 => nums[mid] 在兩段遞增的右段 或 只有一段遞增
同理可應用於 target。

再根據 nums[mid] 和 target 的位置關係，可以決定 target 是否在 nums[mid] 右側：
- F: nums[mid] 在 target 左側的位置
- T: nums[mid] 是 target 以右的位置
則第一個滿足的位置就是第一個 >= target 的位置，最後再檢查該位置是否為 target 即可。
"""


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def check(mid: int) -> bool:  # 檢查 nums[mid] 是否在 target 以右的位置
            # nums[mid] 在兩段遞增的右段 或 只有一段遞增
            if nums[mid] <= nums[-1]:
                # target 在兩段遞增的左段，或在 nums[mid] 以左的位置
                return target > nums[-1] or target <= nums[mid]
            # nums[mid] 在 兩段遞增的左段
            else:
                # target 也在左段，且在 nums[mid] 以左的位置
                return target > nums[-1] and target <= nums[mid]

        left, right = 0, n - 1  # [left, right]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left < n and nums[left] == target else -1


# Solution = Solution1
Solution = Solution2
# @lc code=end
