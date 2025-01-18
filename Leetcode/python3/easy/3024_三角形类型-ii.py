#
# @lc app=leetcode.cn id=3024 lang=python3
#
# [3024] 三角形类型 II
#
from preImport import *
# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        x, y, z = nums
        if x + y <= z:
            return "none"
        # if x == y == z:
        if x == z:
            return "equilateral"
        if x == y or y == z:
            return "isosceles"
        return "scalene"
# @lc code=end

