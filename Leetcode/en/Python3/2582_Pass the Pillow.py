# @algorithm @lc id=2645 lang=python3 
# @title pass-the-pillow


from en.Python3.mod.preImport import *
# @test(4,5)=2
# @test(3,2)=3
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res = time % (2 * (n - 1))
        if res < n:
            return res + 1
        else:
            return 2 * (n - 1) - res + 1
        