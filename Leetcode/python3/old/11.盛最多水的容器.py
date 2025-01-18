#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Two pointers
        Time: O(n)
        Space: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            ans = max(ans, h * w)
            if height[left] <= height[right]:
                # 找到下一個比當前高度h高的
                while(left < right and height[left] <= h): # skip the lower one
                    left += 1
            else:
                while(left < right and height[right] <= h): # skip the lower one
                    right -= 1
        return ans
# @lc code=end
