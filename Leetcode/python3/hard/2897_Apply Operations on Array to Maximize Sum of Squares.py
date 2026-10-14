#
# @lc app=leetcode id=2897 lang=python3
#
# [2897] Apply Operations on Array to Maximize Sum of Squares
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        B = max(nums).bit_length()
        cnt = [0] * B
        for x in nums:
            for b in range(B):
                cnt[b] += (x >> b) & 1
        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(B):
                if cnt[b]:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans += cur * cur
            ans %= MOD
        return ans
# @lc code=end

