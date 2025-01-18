# @algorithm @lc id=3373 lang=python3 
# @title maximum-prime-difference


from en.Python3.mod.preImport import *
# @test([4,2,9,5,3])=3
# @test([4,8,2,8])=0

MAX_N = 105
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False
for i in range(2, MAX_N):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False
            
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        prime = [i for i, x in enumerate(nums) if is_prime[x]]
        if len(prime) < 2:
            return 0
        return prime[-1] - prime[0]