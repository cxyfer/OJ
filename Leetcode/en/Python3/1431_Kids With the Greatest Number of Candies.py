# @algorithm @lc id=1528 lang=python3 
# @title kids-with-the-greatest-number-of-candies


from en.Python3.mod.preImport import *
# @test([2,3,5,1,3],3)=[true,true,true,false,true]
# @test([4,2,1,1,2],1)=[true,false,false,false,false]
# @test([12,1,12],10)=[true,false,true]
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        return [candy + extraCandies >= maxCandy for candy in candies]
        