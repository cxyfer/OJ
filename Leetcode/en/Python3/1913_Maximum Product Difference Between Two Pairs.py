# @algorithm @lc id=2042 lang=python3 
# @title maximum-product-difference-between-two-pairs


from en.Python3.mod.preImport import *
# @test([5,6,2,7,4])=34
# @test([4,2,5,9,7,4,8])=64
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1, mx2 = float('-inf'), float('-inf')
        mn1, mn2 = float('inf'), float('inf')
        for num in nums:
            if num > mx1:
                mx1, mx2 = num, mx1
            elif num > mx2:
                mx2 = num
            if num < mn1:
                mn1, mn2 = num, mn1
            elif num < mn2:
                mn2 = num
        return mx1 * mx2 - mn1 * mn2