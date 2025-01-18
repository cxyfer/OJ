# @algorithm @lc id=66 lang=python3 
# @title plus-one


from en.Python3.mod.preImport import *
# @test([1,2,3])=[1,2,4]
# @test([4,3,2,1])=[4,3,2,2]
# @test([9])=[1,0]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits # 避免進位
        n = len(digits)
        last = n-1
        digits[last] += 1
        while digits[last] >= 10:
            digits[last] -= 10
            last -= 1
            digits[last] += 1
        if digits[0] == 0:
            digits = digits[1:]
        return digits