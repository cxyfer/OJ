#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
from preImport import *
# @lc code=start
class Solution:
    """
        # Two pointers
        Extend from 167. Sum of Two Numbers II - Input Ordered Array
        Similar to 15. 3Sum, 改成枚舉最後一個數字，然後用雙指標找前兩個數字

        left < right < k < n
        TS: O(n log n + n^2) = O(n^2)
        SC: O(1), ignore the space of sorting
    """
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for k in range(2, n): # 枚舉最後一個數字 nums[k]
            c = nums[k]
            left, right = 0, k-1
            while left < right:
                a, b = nums[left], nums[right]
                if a + b > c: # 滿足三角形的條件
                    ans += right - left # a 可以是 nums[left] 到 nums[right-1] 之間的任一個數字，共有 right - left 種可能
                    right -= 1
                else:
                    left += 1
        return ans
# @lc code=end

