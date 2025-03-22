#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        pa = list(range(n))
        sz = [1] * n
        cnt = [0] * n  # number of edges

        def find(x):
            while x != pa[x]:
                pa[x] = pa[pa[x]]
                x = pa[x]
            return x
        
        for x, y in edges:
            fx, fy = find(x), find(y)
            cnt[fx] += 1
            if fx == fy:
                continue
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            pa[fy] = fx
            sz[fx] += sz[fy]
            cnt[fx] += cnt[fy]

        ans = 0
        vis = [False] * n
        for x in range(n):
            fx = find(x)
            if vis[fx]:
                continue
            if sz[fx] * (sz[fx] - 1) == cnt[fx] * 2:
                ans += 1
            vis[fx] = True
        return ans
# @lc code=end

