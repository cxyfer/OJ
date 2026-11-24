#
# @lc app=leetcode id=4122 lang=python3
#
# [4122] Earliest Signal Activation Times
#


# @lcpr-template-start
import re

from preImport import *
# @lcpr-template-end
"""
Weekly Contest 529 - Q3
很像 Dijkstra (但不是) 的 Heap 模擬題
"""
# @lc code=start
class Solution:
    def earliestActivationTimes(self, n: int, edges: list[list[int]], requiredSignals: list[int]) -> list[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        ans = [-1] * n
        cnt = [0] * n
        cnt[0] = requiredSignals[0] - 1

        hp = [(0, 0)]
        while hp:
            d, u = heappop(hp)
            cnt[u] += 1
            if cnt[u] != requiredSignals[u]:  # < 表示數量不足、 > 表示已經發送過
                continue
            ans[u] = d
            for v, w in g[u]:
                heappush(hp, (d + w, v))
        return ans
# @lc code=end

sol = Solution()
print(sol.earliestActivationTimes(5, [[0,3,29],[4,3,2],[0,4,5]], [1,1,1,2,1]))  # [0,-1,-1,29,5]