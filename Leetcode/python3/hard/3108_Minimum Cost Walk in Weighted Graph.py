#
# @lc app=leetcode id=3108 lang=python3
#
# [3108] Minimum Cost Walk in Weighted Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    Greedy + DSU / DFS
    由於代價是路徑上所有邊的 AND ，而 AND 的性質是 A & B <= min(A, B)，且可以重複經過同一條邊多次，
    因此為了使得代價最小，我們可以讓路徑盡可能經過越多的邊，即可以經過連通分量中的所有邊。

    對於每一組詢問 (u, v) ，可以分為以下幾種情況：
    1. u == v ，答案為 0。(但測資中保證不存在這種情況)
    2. u 和 v 在同一個連通分量中，且 u != v ，則答案為該連通分量中的所有邊的 AND 值。
    3. u 和 v 不在同一個連通分量中，則不存在一條從 u 到 v 的路徑，答案為 -1。
"""
# @lc code=start

class Solution1:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        pa = list(range(n))
        sz = [1] * n
        ands = [0xFFFFFFFF] * n  # 該連通分量中的所有邊的 AND 值，初始化為 0xFFFFFFFF

        def find(x):
            while x != pa[x]:
                pa[x] = pa[pa[x]]
                x = pa[x]
            return x

        for u, v, w in edges:
            fx, fy = find(u), find(v)
            ands[fx] &= w
            if fx == fy:
                continue
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            sz[fx] += sz[fy]
            ands[fx] &= ands[fy]
            pa[fy] = fx

        return [ands[find(x)] if find(x) == find(y) else -1 for x, y in query]

class Solution2:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        idxs = [-1] * n  # 每個點所在連通分量的編號，初始化為 -1
        ands = []  # 每個連通分量中所有邊的 AND 值

        def dfs(u: int) -> int:
            res = 0xFFFFFFFF
            idxs[u] = len(ands)  # 紀錄該點所在的連通分量編號
            for v, w in g[u]:
                res &= w
                if idxs[v] >= 0:  # visited
                    continue
                res &= dfs(v)
            return res

        for i in range(n):
            if idxs[i] >= 0:  # visited
                continue
            ands.append(dfs(i))

        return [ands[idxs[x]] if idxs[x] == idxs[y] else -1 for x, y in query]

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.minimumCost(5, [[0, 1, 7],[1, 3, 7],[1, 2, 1]], [[0, 3], [3, 4]]))  # [1,-1]
print(sol.minimumCost(3, [[0, 2, 7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]])) # [0]