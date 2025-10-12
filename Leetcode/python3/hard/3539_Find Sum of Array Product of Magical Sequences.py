#
# @lc app=leetcode id=3539 lang=python3
#
# [3539] Find Sum of Array Product of Magical Sequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
MX = 30

fact = [1] * (MX + 1)
for i in range(2, MX + 1):
    fact[i] = fact[i - 1] * i % MOD
invf = [0] * (MX + 1)
invf[MX] = pow(fact[MX], MOD - 2, MOD)
for i in range(MX, 0, -1):
    invf[i - 1] = invf[i] * i % MOD

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        pow_x = [[1] * (m + 1) for _ in range(n)]
        for i, x in enumerate(nums):
            for j in range(1, m + 1):
                pow_x[i][j] = pow_x[i][j - 1] * x % MOD

        @cache
        def dfs(i, cnt_m, cnt_k, v):
            if i == n:
                return 1 if cnt_m == m and cnt_k + v.bit_count() == k else 0
            res = 0
            for j in range(m + 1 - cnt_m):
                res += pow_x[i][j] * invf[j] * dfs(i + 1, cnt_m + j, cnt_k + ((v + j) & 1), (v + j) >> 1) % MOD
                res %= MOD
            return res
        return dfs(0, 0, 0, 0) * fact[m] % MOD
# @lc code=end

sol = Solution()
print(sol.magicalSum(5, 5, [1,10,100,10000,1000000]))  # 991600007