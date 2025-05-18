#
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 10 ** 9 + 7
M = 3

pow3 = [1] * (M + 1)
for i in range(1, M + 1):
    pow3[i] = pow3[i - 1] * 3

# 生成所有合法狀態
states = []
for s in range(pow3[M]):
    if all(s // pow3[k] % 3 != s // pow3[k + 1] % 3 for k in range(M - 1)):
        states.append(s)

# 生成所有合法狀態的相鄰狀態
nexts = defaultdict(list)
for i, s1 in enumerate(states):
    for s2 in states[:i]:
        if all(s1 // pow3[k] % 3 != s2 // pow3[k] % 3 for k in range(M)):
            nexts[s1].append(s2)
            nexts[s2].append(s1)

class Solution:
    def numOfWays(self, n: int) -> int:
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

