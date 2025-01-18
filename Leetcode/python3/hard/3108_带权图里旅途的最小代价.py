#
# @lc app=leetcode.cn id=3108 lang=python3
#
# [3108] 带权图里旅途的最小代价
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy + DSU / DFS
        由於代價是路徑上所有邊的 AND ，而 AND 的性質是 A & B <= min(A, B)，且可以重複經過同一條邊多次，
        因此為了使得代價最小，我們可以讓路徑盡可能經過越多的邊，即可以經過連通分量中的所有邊。

        對於每一組詢問 (u, v) ，可以分為以下幾種情況：
        1. u == v ，答案為 0。(但測資中不存在這種情況)
        2. u 和 v 在同一個連通分量中，且 u != v ，則答案為該連通分量中的所有邊的 AND 值。
        3. u 和 v 不在同一個連通分量中，則不存在一條從 u 到 v 的路徑，答案為 -1。
    """
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # return self.solve1(n, edges, query)
        return self.solve2(n, edges, query)
    """
        1. DSU
    """
    def solve1(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        pa = list(range(n))
        res = [0xFFFFFFFF] * n # 該連通分量中的所有邊的 AND 值，初始化為 0xFFFFFFFF

        def find(x):
            if x != pa[x]:
                pa[x] = find(pa[x])
            return pa[x]

        for u, v, w in edges:
            u, v = find(u), find(v)
            res[u] &= w
            if u != v:
                res[v] &= res[u]
                pa[u] = v
        
        ans = []
        for x, y in query:
            if x == y:
                ans.append(0)
                continue
            px, py = find(x), find(y)
            ans.append(res[px] if px == py else -1)
        return ans
    """
        2. DFS
    """
    def solve2(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def dfs(u: int) -> int:
            res = 0xFFFFFFFF
            idxs[u] = len(ands) # 紀錄該點所在的連通分量編號
            for v, w in g[u]:
                res &= w
                if idxs[v] < 0: # not visited
                    res &= dfs(v)
            return res
        idxs = [-1] * n # 每個點所在連通分量的編號，初始化為 -1
        ands = [] # 每個連通分量中所有邊的 AND 值
        for i in range(n):
            if idxs[i] < 0: # not visited
                ands.append(dfs(i))
        ans = []
        for x, y in query:
            if x == y:
                ans.append(0)
                continue
            idx1, idx2 = idxs[x], idxs[y]
            ans.append(ands[idx1] if idx1 == idx2 else -1)
        return ans
# @lc code=end
sol = Solution()
print(sol.minimumCost(5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]])) # [1,-1]
print(sol.minimumCost(3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]])) # [0]
