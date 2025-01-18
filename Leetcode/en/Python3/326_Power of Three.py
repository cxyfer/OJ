# @algorithm @lc id=326 lang=python3 
# @title power-of-three


from en.Python3.mod.preImport import *
# @test(27)=true
# @test(0)=false
# @test(-1)=false
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        while n % 3 == 0:
            n //= 3
        return n == 1