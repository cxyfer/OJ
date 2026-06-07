#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
類似於從 153. Find Minimum in Rotated Sorted Array I 到 154. Find Minimum in Rotated Sorted Array II 的轉變，
當陣列中有重複元素時，會影響我們判斷在左段和右段的，只有前綴中與 nums[-1] 相同的元素，
因此本題也可以在 33. Search in Rotated Sorted Array 的基礎上，在保持區間不為空的前提下，將這些元素移除即可。
"""
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
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
        # 在 33. Search in Rotated Sorted Array 的基礎上，移除前綴中與 nums[-1] 相同的元素
        # 注意要避免把所有元素都刪光
        while left < right and nums[left] == nums[-1]:
            left += 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return True if left < n and nums[left] == target else False
# @lc code=end
print(Solution().search([1,0,1,1,1], 0))
print(Solution().search([1,1,1,0,1], 0))