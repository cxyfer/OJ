# @algorithm @lc id=2445 lang=python3 
# @title reachable-nodes-with-restrictions


from en.Python3.mod.preImport import *
# @test(7,[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]],[4,5])=4
# @test(7,[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]],[4,2,1])=3
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # return self.solve1(n, edges, restricted)
        return self.solve2(n, edges, restricted)
    def solve1(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        g = [[] for _ in range(n)]
        for u, v in edges:
            if u in restricted or v in restricted:
                continue
            g[u].append(v)
            g[v].append(u)
        
        ans = 0
        q = deque([(0, -1)]) # (u, fa)
        while q:
            u, fa = q.popleft()
            ans += 1
            for v in g[u]:
                if v == fa:
                    continue
                q.append((v, u))
        return ans
    def solve2(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        g = [[] for _ in range(n)]
        for u, v in edges:
            if u in restricted or v in restricted:
                continue
            g[u].append(v)
            g[v].append(u)
        
        ans = 0
        def dfs(u, fa):
            nonlocal ans
            ans += 1
            for v in g[u]:
                if v == fa:
                    continue
                dfs(v, u)
        dfs(0, -1)
        return ans