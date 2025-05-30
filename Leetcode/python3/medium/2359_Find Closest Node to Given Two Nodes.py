#
# @lc app=leetcode id=2359 lang=python3
# @lcpr version=30204
#
# [2359] Find Closest Node to Given Two Nodes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def get_dist(u: int) -> List[int]:
            dist = [float('inf')] * n
            d = 0
            while u != -1 and dist[u] == float("inf"):
                dist[u] = d
                d += 1
                u = edges[u]
            return dist
        dist = [max(d1, d2) for d1, d2 in zip(get_dist(node1), get_dist(node2))]
        ans = min(range(n), key = lambda x : dist[x])
        return ans if dist[ans] != float("inf") else -1
# @lc code=end

sol = Solution()

#
# @lcpr case=start
# [2,2,3,-1]\n0\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,-1]\n0\n2\n
# @lcpr case=end

#

