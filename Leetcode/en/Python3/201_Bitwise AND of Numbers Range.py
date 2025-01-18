# @algorithm @lc id=201 lang=python3 
# @title bitwise-and-of-numbers-range


from en.Python3.mod.preImport import *
# @test(5,7)=4
# @test(0,0)=0
# @test(1,2147483647)=0
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return self.solve1(left, right) 
        # return self.solve2(left, right)
    def solve1(self, left: int, right: int) -> int:
        n = 0
        while left != right:
            left >>= 1
            right >>= 1
            n += 1
        return left << n
    def solve2(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1) # 消除最低位的1
        return right