# @algorithm @lc id=1817 lang=python3 
# @title calculate-money-in-leetcode-bank


from en.Python3.mod.preImport import *
# @test(4)=10
# @test(10)=37
# @test(20)=96
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        for d in range(n):
            ans += (d // 7 + 1) + (d % 7)
        return ans
        