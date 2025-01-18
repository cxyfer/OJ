# @algorithm @lc id=50 lang=python3 
# @title powx-n


from en.Python3.mod.preImport import *
# @test(2.00000,10)=1024.00000
# @test(2.10000,3)=9.26100
# @test(2.00000,-2)=0.25000
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == float(0):
            return float(0)
        if n < 0:
            x, n = 1 / x, -n
        ans = 1
        while n:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans