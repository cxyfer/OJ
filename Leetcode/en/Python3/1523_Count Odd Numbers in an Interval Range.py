# @algorithm @lc id=1630 lang=python3 
# @title count-odd-numbers-in-an-interval-range


from en.Python3.mod.preImport import *
# @test(3,7)=3
# @test(8,10)=1
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        interval = high - low + 1
        if low & 1 and high & 1:
            return interval // 2 + 1
        else:
            return interval // 2