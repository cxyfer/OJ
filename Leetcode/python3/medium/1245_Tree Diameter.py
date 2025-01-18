#
# @lc app=leetcode id=1245 lang=python3
# @lcpr version=30204
#
# [1245] Tree Diameter
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        def dfs(u: int, fa: int) -> int:
            nonlocal ans
            first = second = 0
            for v in g[u]:
                if v == fa:
                    continue
                length = dfs(v, u) + 1
                if length > first:
                    first, second = length, first
                elif length > second:
                    second = length
            ans = max(ans, first + second)
            return first
        dfs(0, -1)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,1],[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,2],[2,3],[1,4],[4,5]]\n
# @lcpr case=end

#

