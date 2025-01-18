# @algorithm @lc id=2808 lang=python3 
# @title painting-the-walls


from en.Python3.mod.preImport import *
# @test([1,2,3,2],[1,2,3,2])=3
# @test([2,3,4,2],[1,1,1,1])=4
class Solution:
    """
        Dynamic Programming
        Variance of 0-1 knapsack problem
    """
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]