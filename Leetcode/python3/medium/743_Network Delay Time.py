#
# @lc app=leetcode id=743 lang=python3
# @lcpr version=30204
#
# [743] Network Delay Time
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u - 1].append((v - 1, w))
        dist = [float("inf")] * n
        dist[k - 1] = 0
        hp = [(0, k - 1)] # d, u
        while hp:
            d, u = heappop(hp)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                new_d = d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    heappush(hp, (new_d, v))
        return max(dist) if max(dist) != float("inf") else -1
# @lc code=end



#
# @lcpr case=start
# [[2,1,1],[2,3,1],[3,4,1]]\n4\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1]]\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1]]\n2\n2\n
# @lcpr case=end

#

