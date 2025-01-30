#
# @lc app=leetcode id=2493 lang=python3
# @lcpr version=30204
#
# [2493] Divide Nodes Into the Maximum Number of Groups
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        uf = UnionFind(n)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
            uf.union(u, v)

        comps = defaultdict(list)
        for u in range(n):
            comps[uf.find(u)].append(u)

        colors = [-1] * n
        def dfs(u: int, c: int) -> bool:  # 二分圖染色
            colors[u] = c
            for v in g[u]:
                if colors[v] == c:
                    return False
                if colors[v] == -1 and not dfs(v, c ^ 1):
                    return False
            return True
        
        def bfs(u: int) -> int:
            q = deque([u])
            vis = [False] * n
            vis[u] = True
            step = 0
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    for v in g[u]:
                        if vis[v]:
                            continue
                        vis[v] = True
                        q.append(v)
                step += 1
            return step

        ans = 0
        for u, comp in comps.items():
            if not dfs(u, 0):
                return -1
            cur = 0
            for v in comp:
                cur = max(cur, bfs(v))
            ans += cur
        return ans
# @lc code=end

sol = Solution()
print(sol.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
# print(sol.magnificentSets(3, [[1,2],[2,3],[3,1]]))

n = 92
edges = [[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]
print(sol.magnificentSets(n, edges)) # 57
#
# @lcpr case=start
# 6\n[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,2],[2,3],[3,1]]\n
# @lcpr case=end

#

