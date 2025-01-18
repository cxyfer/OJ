# @algorithm @lc id=1950 lang=python3 
# @title sign-of-the-product-of-an-array


from en.Python3.mod.preImport import *
# @test([-1,-2,-3,-4,3,2,1])=1
# @test([1,5,0,2,-3])=0
# @test([-1,1,-1,1,-1])=-1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                ans = 0
                break
            elif num < 0:
                ans *= -1
        return ans