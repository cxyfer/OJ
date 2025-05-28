#
# @lc app=leetcode id=3372 lang=python3
# @lcpr version=30204
#
# [3372] Maximize the Number of Target Nodes After Connecting Trees I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(m)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        def bfs(u, g, t):
            q = deque([u])
            dist = [float("inf")] * len(g)
            dist[u] = 0
            cnt = 0
            while q:
                u = q.popleft()
                if dist[u] > t:
                    break
                cnt += 1
                for v in g[u]:
                    nd = dist[u] + 1
                    if nd < dist[v]:
                        dist[v] = nd
                        q.append(v)
            return cnt
        mx2 = max(bfs(u, g2, k - 1) for u in range(m))
        return [bfs(u, g1, k) + mx2 for u in range(n)]
# @lc code=end
sol = Solution()
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2
print(sol.maxTargetNodes(edges1, edges2, k))  # [9, 7, 9, 8, 8]


#
# @lcpr case=start
# [[0,1],[0,2],[2,3],[2,4]]\n[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,2],[0,3],[0,4]]\n[[0,1],[1,2],[2,3]]\n1\n
# @lcpr case=end

#

