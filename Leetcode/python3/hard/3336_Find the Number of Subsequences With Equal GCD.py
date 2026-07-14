#
# @lc app=leetcode id=3336 lang=python3
# @lcpr version=30204
#
# [3336] Find the Number of Subsequences With Equal GCD
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7

g = [[0] * 201 for _ in range(201)]
for i in range(201):
    for j in range(i + 1):
        g[i][j] = g[j][i] = g[j][i % j] if j else i
gcd = lambda x, y: g[x][y]


class Solution1:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i: int, g1: int, g2: int) -> int:
            if i == n:
                # 也可以只判 g1 == g2，但這樣會多算兩邊都為空的情況，最後需要減掉 1
                return 1 if g1 == g2 and g1 > 0 else 0
            x = nums[i]
            return (dfs(i + 1, g1, g2) + dfs(i + 1, gcd(g1, x), g2) + dfs(i + 1, g1, gcd(g2, x))) % MOD

        return dfs(0, 0, 0)


class Solution2:
    def subsequencePairCount(self, nums: List[int]) -> int:
        U = max(nums)

        f = [[0] * (U + 1) for _ in range(U + 1)]
        f[0][0] = 1
        for x in nums:
            nf = [[0] * (U + 1) for _ in range(U + 1)]
            for g1 in range(U + 1):
                for g2 in range(U + 1):
                    val = f[g1][g2]
                    if val == 0:
                        continue
                    # 都不放/放到A/放到B
                    nf[g1][g2] = (nf[g1][g2] + val) % MOD
                    nf[gcd(g1, x)][g2] = (nf[gcd(g1, x)][g2] + val) % MOD
                    nf[g1][gcd(g2, x)] = (nf[g1][gcd(g2, x)] + val) % MOD
            f = nf
        return sum(f[g][g] for g in range(1, U + 1)) % MOD


Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.subsequencePairCount([1, 2, 3, 4]))  # 10
print(sol.subsequencePairCount([10, 20, 30]))  # 2
print(sol.subsequencePairCount([1, 1, 1, 1]))  # 50
print(sol.subsequencePairCount([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 32, 64, 64, 64, 128, 128, 128, 128, 128, 128, 128]))  # 1000000006