#
# @lc app=leetcode id=3965 lang=python3
#
# [3965] Finish Time of Tasks I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
DFS / 樹形DP
令 f[u] 表示以 u 為根的子樹完成任務所需的最短時間，根據題意，轉移式如下
- 如果 u 是葉子節點，f[u] = baseTime[u]
- 否則 f[u] = max(f[v]) + (max(f[v]) - min(f[v])) + baseTime[u]
在 DFS 過程中計算 f[u]，最後返回 f[0] 即可。
"""
# @lc code=start
class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)

        f = baseTime[:]

        def dfs(u: int) -> None:
            if not g[u]:  # Leaf
                return
            mx, mn = -inf, inf
            for v in g[u]:
                dfs(v)
                mx = max(mx, f[v])
                mn = min(mn, f[v])
            f[u] += mx + (mx - mn)

        dfs(0)
        return f[0]
# @lc code=end

