#
# @lc app=leetcode id=2192 lang=python3
# @lcpr version=30204
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)

        def dfs(st:int, u: int) -> None:
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    ans[v].append(st)
                    dfs(st, v)

        ans = [[] for _ in range(n)]
        for st in range(n):
            visited = [False] * n
            dfs(st, st)
        return ans
# @lc code=end



#
# @lcpr case=start
# 8\n[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]\n
# @lcpr case=end

#

