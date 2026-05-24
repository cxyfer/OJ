#
# @lc app=leetcode id=3939 lang=python3
#
# [3939] Count Non Adjacent Subsets in a Rooted Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)


class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        n = len(nums)

        g = [[] for _ in range(n)]
        for u, fa in enumerate(parent):
            if fa != -1:
                g[fa].append(u)

        def dfs(u: int):
            f = [[0] * k for _ in range(2)]

            f[0][0] = 1
            f[1][nums[u] % k] = 1

            for v in g[u]:
                fv = dfs(v)
                nf = [[0] * k for _ in range(2)]
                for r1 in range(k):
                    if f[0][r1] == 0:
                        continue
                    for r2 in range(k):
                        nr = (r1 + r2) % k
                        nf[0][nr] += f[0][r1] * (fv[0][r2] + fv[1][r2]) % MOD
                        nf[0][nr] %= MOD
                for r1 in range(k):
                    if f[1][r1] == 0:
                        continue
                    for r2 in range(k):
                        nr = (r1 + r2) % k
                        nf[1][nr] += f[1][r1] * fv[0][r2]
                        nf[1][nr] %= MOD
                f = nf
            return f

        f = dfs(0)

        return (sum(f[b][0] for b in range(2)) - 1) % MOD
# @lc code=end
sol = Solution()
print(sol.countValidSubsets([-1,0,1], [1,2,3], 3))  # 1
print(sol.countValidSubsets([-1,0,0,0], [2,1,2,1], 3))  # 2