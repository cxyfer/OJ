#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        x, y, z = nums
        if x + y <= z:
            return "none"
        elif x == y == z:
            return "equilateral"
        elif x == y or y == z:
            return "isosceles"
        else:
            return "scalene"
# @lc code=end

