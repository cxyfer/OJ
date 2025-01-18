# @algorithm @lc id=2756 lang=python3 
# @title buy-two-chocolates


from en.Python3.mod.preImport import *
# @test([1,2,2],3)=0
# @test([3,2,3],3)=3
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float('inf')
        for p in prices:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p
        return money - (min1 + min2) if money >= min1 + min2 else money