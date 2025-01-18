# @algorithm @lc id=3394 lang=python3 
# @title minimum-array-end


from en.Python3.mod.preImport import *
# @test(3,4)=6
# @test(2,7)=15
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        i = j = 0
        while n:
            if not x & (1 << i): # x 的第 i 位是 0，可以填充
                if n & (1 << j): # n 的第 j 位是 1，需要填充
                    ans |= (1 << i)
                    n -= (1 << j)
                j += 1
            i += 1
        return ans