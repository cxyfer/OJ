# @algorithm @lc id=2752 lang=python3 
# @title sum-multiples


from en.Python3.mod.preImport import *
# @test(7)=21
# @test(10)=40
# @test(9)=30
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for num in range(2, n+1):
            for prime in [3, 5, 7]:
                if num % prime == 0:
                    ans += num
                    break
        return ans