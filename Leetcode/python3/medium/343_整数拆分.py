#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
from preImport import *
# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # return self.solveByMath(n)
        return self.solveByDP(n)
    
    """
        1. Math
            n = 2: 1 * 1 = 1
            n = 3: 1 * 2 = 2
            n = 4: 2 * 2 = 4
            n = 5: 2 * 3 = 6
            n = 6: 3 * 3 = 9
            n = 7: 3 * 2 * 2 = 12
        除了2,3,4都可以拆分成2和3的和，因此我們只考慮n >= 5的情況，優先選3，如果剩下的是4，則選4
    """
    def solveByMath(self, n: int) -> int:
        if n == 0: return 0
        elif n <= 3: return n - 1
        elif n % 3 == 0: # 都是3
            return int(math.pow(3, n // 3))
        elif n % 3 == 1: # 剩餘4
            return 4 * int(math.pow(3, (n-4) // 3))
        else: # 剩餘2
            return 2 * int(math.pow(3, (n-2) // 3))
    """
        2. DP
    """
    def solveByDP(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(i): # 拆出j和i-j
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        return dp[n]
# @lc code=end

