#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # f[i][b][j] 表示考慮前 i 個元素，最後為連續 j 個 b 的子序列數量
        # f = [[[0, 0] for _ in range(2)] for _ in range(n + 1)]
        f = [[0, 0] for _ in range(2)]
        for i, x in enumerate(nums, 1):
            b = x & 1
            f[b][1] = (f[b][1] + f[b][0]) % MOD
            f[b][0] = (f[b][0] + f[b ^ 1][0] + f[b ^ 1][1] + 1) % MOD
        return sum(map(sum, f)) % MOD
# @lc code=end
sol = Solution()
print(sol.countStableSubsequences([1,3,5]))  # 6
print(sol.countStableSubsequences([2,3,4,2]))  # 14
