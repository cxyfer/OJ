#
# @lc app=leetcode id=1931 lang=python3
#
# [1931] Painting a Grid With Three Different Colors
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
三進位狀態壓縮DP
"""
# @lc code=start
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        pow3 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow3[i] = pow3[i - 1] * 3

        # 生成所有合法狀態
        states = []
        for s in range(pow3[m]):
            if all(s // pow3[k] % 3 != s // pow3[k + 1] % 3 for k in range(m - 1)):
                states.append(s)

        # 生成所有合法狀態的相鄰狀態
        nexts = defaultdict(list)
        for i, s1 in enumerate(states):
            for s2 in states[:i]:
                if all(s1 // pow3[k] % 3 != s2 // pow3[k] % 3 for k in range(m)):
                    nexts[s1].append(s2)
                    nexts[s2].append(s1)

        @cache
        def dfs(i, s):
            if i == n:
                return 1
            res = 0
            for ns in nexts[s]:
                res = (res + dfs(i + 1, ns)) % MOD
            return res

        ans = 0
        for s in states:
            ans = (ans + dfs(1, s)) % MOD
        return ans
# @lc code=end

sol = Solution()
print(sol.colorTheGrid(1, 1))
print(sol.colorTheGrid(1, 2))
print(sol.colorTheGrid(5, 5))