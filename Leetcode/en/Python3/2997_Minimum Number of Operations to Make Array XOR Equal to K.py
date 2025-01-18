# @algorithm @lc id=3249 lang=python3 
# @title minimum-number-of-operations-to-make-array-xor-equal-to-k


from en.Python3.mod.preImport import *
# @test([2,1,3,4],1)=2
# @test([2,0,2,0],0)=0
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for num in nums:
            x ^= num
        ans = 0
        while x or k:
            if x & 1 != k & 1:
                ans += 1
            x >>= 1
            k >>= 1
        return ans