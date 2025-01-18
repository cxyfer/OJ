# @algorithm @lc id=2491 lang=python3 
# @title smallest-even-multiple


from en.Python3.mod.preImport import *
# @test(5)=10
# @test(6)=6
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2