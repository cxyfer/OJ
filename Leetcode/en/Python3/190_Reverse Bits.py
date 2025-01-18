# @algorithm @lc id=190 lang=python3 
# @title reverse-bits


from en.Python3.mod.preImport import *
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= (n & 1) << (31 - i)
            n >>= 1
        return ans