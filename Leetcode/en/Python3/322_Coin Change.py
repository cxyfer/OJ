# @algorithm @lc id=322 lang=python3 
# @title coin-change


from en.Python3.mod.preImport import *
# @test([1,2,5],11)=3
# @test([2],3)=-1
# @test([1],0)=0
class Solution:
    """
        Dynamic Programming
        dp[i] 表示湊成i所需的最少硬幣數量
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c]+1)
                else:
                    break
        return dp[-1] if dp[-1] != float('inf') else -1
        