#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
max = lambda a, b : a if a > b else b
min = lambda a, b : a if a < b else b
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        while left < right:
            h = min(height[left], height[right])
            ans = max(ans, h * (right - left))
            if height[left] <= height[right]:
                while (left < right and height[left] <= h):
                    left += 1
            else:
                while (left < right and height[right] <= h):
                    right -= 1
        return ans
# @lc code=end

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,2,4,3]))  # 4