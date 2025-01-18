#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from typing import *
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for idx in range(1, target+1):
            for num in nums:
                if idx >= num:
                    dp[idx] += dp[idx-num]
        return dp[-1]
# @lc code=end

