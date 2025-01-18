# @algorithm @lc id=922 lang=python3 
# @title possible-bipartition


from en.Python3.mod.preImport import *
# @test(4,[[1,2],[1,3],[2,4]])=true
# @test(3,[[1,2],[1,3],[2,3]])=false
class Solution:
    """
        二分圖判斷：DFS / BFS / Disjoint Set
        https://zhuanlan.zhihu.com/p/161082172
        Similar to ABC327_D: Good Tuple Problem
    """
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n+1)]
        for u, v in dislikes:
            g[u].append(v)
            g[v].append(u)
        colors = [0] * (n+1) # 0: not colored, 1/-1: colored

        for u in range(1, n+1):
            if colors[u] == 0: # not colored
                stack = [(u, 1)] # (node, color)
                colors[u] = 1
                while stack:
                    u, color = stack.pop()
                    for v in g[u]:
                        if colors[v] == 0: # not colored
                            stack.append((v, -color))
                            colors[v] = -color
                        elif colors[v] == color:
                            return False
        return True