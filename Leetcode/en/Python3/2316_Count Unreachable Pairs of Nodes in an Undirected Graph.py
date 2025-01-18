# @algorithm @lc id=2403 lang=python3 
# @title count-unreachable-pairs-of-nodes-in-an-undirected-graph


from en.Python3.mod.preImport import *
# @test(3,[[0,1],[0,2],[1,2]])=0
# @test(7,[[0,2],[0,5],[2,4],[1,6],[5,4]])=14
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # return self.solveByDFS(n, edges)
        return self.solveByDisjointSet(n, edges)
    """
        1. DFS
    """
    def solveByDFS(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n

        def dfs(i): # return the size of the connected component
            visited[i] = True
            size = 1
            for j in graph[i]:
                if not visited[j]:
                    size += dfs(j)
            return size
        ans = total = 0
        for i in range(n):
            if not visited[i]:
                size = dfs(i)
                ans += total * size
                total += size
        return ans
    """
        2. Disjoint Set
    """
    def solveByDisjointSet(self, n: int, edges: List[List[int]]) -> int:
        disjoint_set = [-1 for i in range(n)]
        def find(x):
            if disjoint_set[x] < 0:
                return x
            disjoint_set[x] = find(disjoint_set[x])
            return disjoint_set[x]
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            disjoint_set[y] = x
            return True
        for u, v in edges:
            union(u, v)
        cnt = Counter()
        for i in range(n):
            cnt[find(i)] += 1
        # O(n)
        ans = total = 0
        for i in cnt: 
            ans += total * cnt[i]
            total += cnt[i]
        # O(n^2) -> TLE
        # m = len(cnt)
        # nums = list(cnt.values())
        # for i in range(m):
        #     for j in range(i+1, m):
        #         ans += nums[i] * nums[j]
        return ans