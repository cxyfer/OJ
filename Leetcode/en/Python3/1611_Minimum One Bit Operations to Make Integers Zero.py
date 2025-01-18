# @algorithm @lc id=1732 lang=python3 
# @title minimum-one-bit-operations-to-make-integers-zero


from en.Python3.mod.preImport import *
# @test(3)=2
# @test(6)=4
class Solution:
    """
        Gray code
    """
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans ^= n
            n >>= 1
        return ans
