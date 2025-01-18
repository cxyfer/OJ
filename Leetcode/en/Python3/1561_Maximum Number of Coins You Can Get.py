# @algorithm @lc id=1683 lang=python3 
# @title maximum-number-of-coins-you-can-get


from en.Python3.mod.preImport import *
# @test([2,4,1,2,7,8])=9
# @test([2,4,5])=4
# @test([9,8,7,6,5,1,2,3,4])=18
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans += piles[2*i+1]
        return ans