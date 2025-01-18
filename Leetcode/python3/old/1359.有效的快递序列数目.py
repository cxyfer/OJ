#
# @lc app=leetcode.cn id=1359 lang=python3
#
# [1359] 有效的快递序列数目
#
from en.Python3.mod.preImport import *
# @lc code=start
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
# @lc code=end

