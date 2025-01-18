# @algorithm @lc id=367 lang=python3 
# @title valid-perfect-square


from en.Python3.mod.preImport import *
# @test(16)=true
# @test(14)=false
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while (left <= right): # [left, right]
            middle = left + (right-left)//2
            if middle*middle == num:
                return True
            elif middle*middle < num:
                left = middle + 1
            else:
                right = middle - 1
        return False