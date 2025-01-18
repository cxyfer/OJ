# @algorithm @lc id=2652 lang=python3 
# @title count-number-of-possible-root-nodes


from en.Python3.mod.preImport import *
# @test([[0,1],[1,2],[1,3],[4,2]],[[1,3],[0,1],[1,0],[2,4]],3)=3
# @test([[0,1],[1,2],[2,3],[3,4]],[[1,0],[3,4],[2,1],[3,2]],1)=5
class Solution:
    """
        記憶化搜索DP / 換根DP
    """
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        st = set([(u, v) for u, v in guesses])
        
        # @cache # 若用換根DP，只會執行一次DFS，因此不需要memoization
        def dfs(u: int, fa: int) -> int:
            res = 0
            for v in g[u]:
                if v == fa: continue
                if (u, v) in st:
                    res += 1 # 對於這條邊的父子關係，猜對了
                res += dfs(v, u) 
            return res
        
        def solve1() -> int: # 1. 記憶化搜索DP
            ans = 0
            for i in range(n):
                ans += (dfs(i, -1) >= k)
            return ans

        def reroot(x: int, fa: int, cnt: int) -> int: # 再執行一次DFS來做換根
            ans = (cnt >= k) # 此時 cnt 為以 x 為根時的猜對數量，若滿足條件則答案+1
            for y in g[x]:
                if y == fa: continue
                ans += reroot(y, x, cnt - ((x, y) in st) + ((y, x) in st)) # 改以 y 為根時，猜對數量的變化
            return ans
        cnt0 = dfs(0, -1) # 以 0 為根時的猜對數量
        return reroot(0, -1, cnt0)