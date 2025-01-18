# @algorithm @lc id=1406 lang=python3 
# @title subtract-the-product-and-sum-of-digits-of-an-integer


from en.Python3.mod.preImport import *
# @test(234)=15
# @test(4421)=21
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ans1, ans2 = 1, 0
        while(n > 0):
            d = n % 10
            ans1 *= d
            ans2 += d
            n //= 10
        return ans1 - ans2
        