# @algorithm @lc id=11 lang=python3 
# @title container-with-most-water


from en.Python3.mod.preImport import *
# @test([1,8,6,2,5,4,8,3,7])=49
# @test([1,1])=1
class Solution:
    """
        Two pointers

        TS: O(n)
        SC: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        while (left < right): # 至少有兩個柱子
            h = min(height[left], height[right])
            w = right - left
            ans = max(ans, h * w)
            # 找到下一個比當前高度h高的
            if height[left] <= height[right]:
                while (left < right and height[left] <= h): # skip the lower one
                    left += 1
            else:
                while (left < right and height[right] <= h): # skip the lower one
                    right -= 1
        return ans