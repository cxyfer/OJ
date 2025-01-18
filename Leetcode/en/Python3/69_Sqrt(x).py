# @algorithm @lc id=69 lang=python3 
# @title sqrtx


from en.Python3.mod.preImport import *
# @test(4)=2
# @test(8)=2
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while (left <= right): # [left, right]
            middle = left + (right-left)//2
            if middle*middle == x:
                return middle
            elif middle*middle < x:
                left = middle + 1
            else:
                right = middle - 1
        return right