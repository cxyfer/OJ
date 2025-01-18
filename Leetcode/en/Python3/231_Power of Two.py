# @algorithm @lc id=231 lang=python3 
# @title power-of-two


from en.Python3.mod.preImport import *
# @test(1)=true
# @test(16)=true
# @test(3)=false
# @test(1)=true
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        # return n > 0 and (n & -n) == n  