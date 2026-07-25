#
# @lc app=leetcode id=3995 lang=python3
#
# [3995] Minimum Cost to Convert String III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)

        for i, (pattern, _) in enumerate(rules):
            costs[i] += pattern.count("*")

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0

            res = inf if source[i] != target[i] else dfs(i + 1)
            for (pattern, replacement), cost in zip(rules, costs):
                m = len(pattern)
                if i + m > n or replacement != target[i : i + m]:
                    continue
                for j, ch in enumerate(pattern):
                    if ch != "*" and ch != source[i + j]:
                        break
                else:
                    res = min(res, cost + dfs(i + m))
            return res

        ans = dfs(0)
        dfs.cache_clear()
        return ans if ans != inf else -1
# @lc code=end

