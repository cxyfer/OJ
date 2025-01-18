# @algorithm @lc id=1610 lang=python3 
# @title xor-operation-in-an-array


from en.Python3.mod.preImport import *
# @test(5,0)=8
# @test(4,3)=8
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            ans ^= (start + 2 * i)
        return ans
        