#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        pa = list(range(n))
        sz_v = [1] * n
        sz_e = [0] * n  # number of edges

        def find(x):
            while pa[x] != x:
                pa[x] = pa[pa[x]]
                x = pa[x]
            return x

        for x, y in edges:
            fx, fy = find(x), find(y)
            sz_e[fx] += 1
            if fx == fy:
                continue
            if sz_v[fx] < sz_v[fy]:
                fx, fy = fy, fx
            pa[fy] = fx
            sz_v[fx] += sz_v[fy]
            sz_e[fx] += sz_e[fy]

        ans = 0
        vis = [False] * n
        for x in range(n):
            fx = find(x)
            if vis[fx]:
                continue
            vis[fx] = True
            if sz_v[fx] * (sz_v[fx] - 1) == sz_e[fx] << 1:
                ans += 1
        return ans


class Solution2:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n

        def dfs(u: int) -> Tuple[int, int]:
            vis[u] = True
            cnt_v, cnt_e = 1, len(g[u])
            for v in g[u]:
                if vis[v]:
                    continue
                sub_v, sub_e = dfs(v)
                cnt_v += sub_v
                cnt_e += sub_e
            return cnt_v, cnt_e

        ans = 0
        for u in range(n):
            if vis[u]:
                continue
            cnt_v, cnt_e = dfs(u)
            if cnt_v * (cnt_v - 1) == cnt_e:
                ans += 1
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

