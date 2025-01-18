# @algorithm @lc id=1461 lang=python3 
# @title count-all-valid-pickup-and-delivery-options


from en.Python3.mod.preImport import *
# @test(1)=1
# @test(2)=6
# @test(3)=90
class Solution:
    """
        DP & Combination
        P(n) = P(n-1) * (C(2n-1, 2) + C(2n-1, 1))
    """
    def countOrders(self, n: int) -> int:
        MOD = 1000000007
        ans = 1 # base case: n=1
        for i in range(2, n+1):
            cur = math.comb(2*i-1, 2) + math.comb(2*i-1, 1)
            ans = ans * cur % MOD
        return ans