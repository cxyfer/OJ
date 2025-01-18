#
# @lc app=leetcode.cn id=2867 lang=python3
#
# [2867] 统计树中的合法路径数目
#
from preImport import *
# @lc code=start

# Initialize the list of prime numbers for each number
MAXN = 10 ** 5 + 5
isPrime = [True] * MAXN
isPrime[0] = isPrime[1] = False
for i in range(2, math.isqrt(MAXN) + 1):
    if isPrime[i]: # i is prime
        for j in range(i*i, MAXN, i): # mark all multiples of i
            isPrime[j] = False
            
class Solution:
    """
        Note that the tree is undirected, so we can start from any node.
        Prime Detection + Disjoint Set Union(DSU) / DFS + Multiplication Principle
    """
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # return self.solve1(n, edges)
        return self.solve2(n, edges)
    """
        1. DSU
    """
    def solve1(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 用 Disjoint Set Union(DSU) 計算所有非質數節點的連通分量大小
        pa = list(range(n + 1)) # parent

        def find(x: int) -> int: # find root
            if pa[x] != x:
                pa[x] = find(pa[x])
            return pa[x]

        size = [1] * (n + 1) # size of connected component
        for x in range(1, n + 1):
            if isPrime[x]:
                continue
            fx = find(x)
            for y in g[x]:
                if isPrime[y]:
                    continue
                fy = find(y)
                if fy == fx:
                    continue
                size[fx] += size[fy] # 以 x 為根節點合併
                pa[fy] = fx
        ans = 0
        for x in range(1, n+1): # 枚舉所有質數節點 x
            if not isPrime[x]:
                continue
            cur = 0 # 起點數量
            for y in g[x]: # 枚舉與 x 相鄰的非質數節點 y
                if isPrime[y]:
                    continue
                fy = find(y)
                ans += cur * size[fy] # 乘法原理：起點數量 * 終點數量
                cur += size[fy]
            ans += cur # 以 x 為終點
        return ans
    """
        2. DFS
    """
    def solve2(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(x: int, pa: int) -> None:
            nodes.append(x)
            for y in g[x]:
                if y == pa or isPrime[y]:
                    continue
                dfs(y, x)

        ans = 0
        size = [0] * (n + 1) # size of connected component
        for x in range(1, n+1): # 枚舉所有質數節點 x
            if not isPrime[x]:
                continue
            cur = 0 # 起點數量
            for y in g[x]: # 枚舉與 x 相鄰的非質數節點 y
                if isPrime[y]:
                    continue
                if size[y] == 0: # y 所在的連通分量尚未被計算過
                    nodes = []
                    dfs(y, -1)
                    for z in nodes: # 將該連通分量的所有非質數節點的 size 設為該連通分量的大小
                        size[z] = len(nodes)
                ans += cur * size[y] # 乘法原理：起點數量 * 終點數量
                cur += size[y]
            ans += cur # 以 x 為終點
        return ans
# @lc code=end
sol = Solution()
# @test(5,[[1,2],[1,3],[2,4],[2,5]])=4
# @test(6,[[1,2],[1,3],[2,4],[3,5],[3,6]])=6
print(sol.countPaths(5,[[1,2],[1,3],[2,4],[2,5]])) # 4
print(sol.countPaths(6,[[1,2],[1,3],[2,4],[3,5],[3,6]])) # 6
print(sol.countPaths(10, [[2,9],[3,9],[8,9],[10,3],[1,9],[4,8],[7,10],[6,1],[5,10]])) # 18