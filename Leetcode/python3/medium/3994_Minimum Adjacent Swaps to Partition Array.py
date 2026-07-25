#
# @lc app=leetcode id=3994 lang=python3
#
# [3994] Minimum Adjacent Swaps to Partition Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7


class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        ans = 0
        cnt = [0] * 3
        for x in nums:
            x = 0 if x < a else (2 if x > b else 1)
            if x == 0:
                ans += cnt[1] + cnt[2]
            elif x == 1:
                ans += cnt[2]
            cnt[x] += 1
        return ans % MOD
# @lc code=end

