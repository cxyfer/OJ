#
# @lc app=leetcode id=3897 lang=python3
#
# [3897] Maximum Value of Concatenated Binary Segments
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
MAX_N = int(2e5 + 5)
pow2 = [1] * MAX_N
for i in range(1, MAX_N):
    pow2[i] = pow2[i - 1] * 2 % MOD


class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        segs = []
        for a, b in zip(nums1, nums0):
            segs.append((a, b))

        segs.sort(key=lambda x: (x[1] > 0, -x[0], x[1]))

        ans = 0
        for a, b in segs:
            ans = (ans * pow2[a] + (pow2[a] - 1)) % MOD
            ans = (ans * pow2[b]) % MOD
        return ans
# @lc code=end
