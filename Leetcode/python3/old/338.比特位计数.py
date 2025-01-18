#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
from en.Python3.mod.preImport import *
# @lc code=start
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
# @lc code=end

