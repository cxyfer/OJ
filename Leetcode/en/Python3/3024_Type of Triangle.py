# @algorithm @lc id=3321 lang=python3 
# @title type-of-triangle


from en.Python3.mod.preImport import *
# @test([3,3,3])="equilateral"
# @test([3,4,5])="scalene"
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