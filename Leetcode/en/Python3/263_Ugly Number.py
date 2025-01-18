# @algorithm @lc id=263 lang=python3 
# @title ugly-number


from en.Python3.mod.preImport import *
# @test(6)=true
# @test(1)=true
# @test(14)=false
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor

        return n == 1
