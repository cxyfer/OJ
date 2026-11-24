#
# @lc app=leetcode id=4116 lang=python3
#
# [4116] Assign Umbrella on Rainy Days
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Biweekly Contest 196 - Q1
簡單模擬
"""
# @lc code=start
class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        n = len(rain)
        ans = [None] * n
        cntA = cntB = 0
        for i, x in enumerate(rain):
            if x == 0:
                ans[i] = "None"
            else:
                if cntA <= cntB and (i < n - 1 and rain[i + 1] == 1):
                    ans[i] = "Alice"
                    cntA += 1
                else:
                    ans[i] = "Bob"
                    cntB += 1
        return ans
# @lc code=end

