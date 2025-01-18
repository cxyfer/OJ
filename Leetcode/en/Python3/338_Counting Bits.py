# @algorithm @lc id=338 lang=python3 
# @title counting-bits

from en.Python3.mod.preImport import *
# @test(2)=[0,1,1]
# @test(5)=[0,1,1,2,1,2]
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
            Dynamic Programming
            - 奇數的1個數目 = 前一個數(偶數)的1個數目 + 1
                - f(1101) = f(1100) + 1
            - 偶數的1個數目 = 偶數/2的1個數目
                - f(1110) = f(111)
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i - 1] + 1
        return dp