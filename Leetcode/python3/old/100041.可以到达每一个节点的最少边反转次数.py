#
# @lc app=leetcode.cn id=100041 lang=python3
#
# [100041] 可以到达每一个节点的最少边反转次数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        換根DP
        Similar to 834. Sum of Distances in Tree
        固定一個點為根節點
    """
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append((v, True)) # True: 正向邊
            graph[v].append((u, False)) # False: 反向邊
        # DP
        ans = [0] * n
        def dfs(x: int, parent: int) -> None:
            for y, isForward in graph[x]:
                if y != parent:
                    ans[0] += 1 if not isForward else 0
                    dfs(y, x) # 令y為根節點，x為父節點
        dfs(0, -1) # 令0為根節點，且沒有父節點

        def reroot(x: int, parent: int) -> None:
            for y, isForward in graph[x]:
                if y != parent:
                    ans[y] = ans[x] + (1 if isForward else -1)
                    reroot(y, x) # 令y為根節點，x為父節點
        reroot(0, -1) # 令0為根節點，且沒有父節點

        return ans
# @lc code=end

