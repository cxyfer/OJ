#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        DFS
        a/d = a/b * b/c * c/d
    """
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 建立相鄰表，反向邊的權重為原權重的倒數
        adj = defaultdict(lambda: defaultdict(float))
        for (x, y), val in zip(equations, values):
            adj[x][y] = val
            adj[y][x] = 1/val
        # 用DFS找u到v的路徑，若找不到則回傳-1，若找到則回傳路徑上的權重乘積
        def dfs(u, v): # u/v
            if u not in adj:
                return -1
            if u == v:
                return 1
            for node in adj[u]:
                if node == v: # u可以直接到v
                    return adj[u][node]
                elif node not in visited: # u可以到node，node可以到v
                    visited.add(node)
                    res = dfs(node, v)
                    if res != -1:
                        return adj[u][node]*res
            return -1
        # 對每個query做DFS
        ans = []
        for u, v in queries:
            visited = set()
            ans.append(dfs(u, v))
        return ans
# @lc code=end

sol = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(sol.calcEquation(equations, values, queries))

