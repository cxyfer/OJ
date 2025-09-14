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
class Solution1:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # f[i][b][j] 表示考慮前 i 個元素，最後為連續 j 個 b 的子序列數量
        # f = [[[0, 0] for _ in range(2)] for _ in range(n + 1)]
        f = [[0, 0] for _ in range(2)]
        for i, x in enumerate(nums, 1):
            b = x & 1
            f[b][1] = (f[b][1] + f[b][0]) % MOD
            f[b][0] = (f[b][0] + f[b ^ 1][0] + f[b ^ 1][1] + 1) % MOD
        return sum(map(sum, f)) % MOD

class Solution2:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # f[i][b1][b2] 表示考慮前 i 個元素，最後兩個元素分別為 b1 和 b2 ，且不出現超過連續三個相同元素的子序列數量
        # 特別地，用 f[2][b] 來表示長度為 1，且最後一個元素為 b 的子序列數量
        f = [[0, 0, 0] for _ in range(3)]
        for x in nums:
            b = x & 1
            f[b][b] += (f[b ^ 1][b] + f[2][b])
            f[b][b] %= MOD
            f[b ^ 1][b] += (f[0][b ^ 1] + f[1][b ^ 1] + f[2][b ^ 1])
            f[b ^ 1][b] %= MOD
            f[2][b] += 1
            # if b == 0:  # 拆開來會比較好懂
            #     f[0][0] += (f[1][0] + f[2][0])
            #     f[0][0] %= MOD
            #     f[1][0] += (f[0][1] + f[1][1] + f[2][1])
            #     f[1][0] %= MOD
            #     f[2][0] += 1
            # else:
            #     f[1][1] += (f[0][1] + f[2][1])
            #     f[1][1] %= MOD
            #     f[0][1] += (f[0][0] + f[1][0] + f[2][0])
            #     f[0][1] %= MOD
            #     f[2][1] += 1
        return sum(map(sum, f)) % MOD

# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.countStableSubsequences([1,3,5]))  # 6
print(sol.countStableSubsequences([2,3,4,2]))  # 14
