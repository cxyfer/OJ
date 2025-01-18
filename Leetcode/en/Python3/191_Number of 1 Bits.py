# @algorithm @lc id=191 lang=python3 
# @title number-of-1-bits


from en.Python3.mod.preImport import *
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans