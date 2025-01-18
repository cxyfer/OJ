# @algorithm @lc id=403 lang=python3 
# @title frog-jump


from en.Python3.mod.preImport import *
# @test([0,1,3,5,6,8,12,17])=true
# @test([0,1,2,3,4,8,9,11])=false
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # DP
        n = len(stones)
        # dp[i][k] 表示青蛙能否跳到第i塊石頭上，且上次跳躍距離為k
        # 因為最多只能跳n-1步，且第1步為1，所以走到第n-1塊石頭(終點)時，k最大為n-1
        # 轉移方程為：dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        # 先排除一些不可能的情況，若第i+1塊石頭與第i塊的石頭的距離大於i，則不可能跳到終點
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False
        # 開始DP
        for i in range(1, n):
            for j in range(i-1, -1, -1): # j為上一塊石頭的下標
                k = stones[i] - stones[j] # k為上一次跳躍的距離
                # 在第j塊石頭上最多只能跳j+1步，若 k > j+1 則不可能從第j塊石頭跳到第i塊石頭
                if k > j + 1: 
                    break
                dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
        return any(dp[-1]) # 若能走到終點