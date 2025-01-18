# @algorithm @lc id=1574 lang=python3 
# @title maximum-product-of-two-elements-in-an-array


from en.Python3.mod.preImport import *
# @test([3,4,5,2])=12
# @test([1,5,4,5])=16
# @test([3,7])=12
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1 = mx2 = -1
        for num in nums:
            if num > mx1:
                mx1, mx2 = num, mx1
            elif num > mx2:
                mx2 = num
        return (mx1 - 1) * (mx2 - 1)
    