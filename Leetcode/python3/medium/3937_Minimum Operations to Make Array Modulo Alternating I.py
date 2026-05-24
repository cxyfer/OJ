#
# @lc app=leetcode id=3937 lang=python3
#
# [3937] Minimum Operations to Make Array Modulo Alternating I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        cnts = [defaultdict(int) for _ in range(2)]
        for i, x in enumerate(nums):
            cnts[i & 1][x % k] += 1

        res = [[inf] * k for _ in range(2)]
        for b, cnt in enumerate(cnts):
            for tgt in range(k):
                cur = 0
                for v, c in cnt.items():
                    d = abs(v - tgt)
                    cur += min(d, k - d) * c
                res[b][tgt] = cur

        ans = inf
        for x in range(k):
            for y in range(k):
                if x == y:
                    continue
                ans = min(ans, res[0][x] + res[1][y])
        return ans
# @lc code=end

