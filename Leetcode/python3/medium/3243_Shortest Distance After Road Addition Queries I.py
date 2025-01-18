#
# @lc app=leetcode id=3243 lang=python3
# @lcpr version=30204
#
# [3243] Shortest Distance After Road Addition Queries I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append(i + 1)
        vis = [-1] * n

        ans = [-1] * len(queries)
        for i, (u, v) in enumerate(queries):
            g[u].append(v)

            q = deque([(0, 0)])
            vis[0] = i
            while q:
                u, d = q.popleft()
                if u == n - 1:
                    ans[i] = d
                    break
                for v in g[u]:
                    if vis[v] != i:
                        vis[v] = i
                        q.append((v, d + 1))
        return ans
# @lc code=end



#
# @lcpr case=start
# 5\n[[2,4],[0,2],[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,3],[0,2]]\n
# @lcpr case=end

#

