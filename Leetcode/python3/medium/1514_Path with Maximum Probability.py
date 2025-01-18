#
# @lc app=leetcode id=1514 lang=python3
# @lcpr version=30204
#
# [1514] Path with Maximum Probability
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for (u, v), w in zip(edges, succProb):
            g[u].append((v, w))
            g[v].append((u, w))
        prob = [0] * n
        prob[start_node] = 1
        hp = [(-1, start_node)] # Max heap: (prob, node)
        while hp:
            p, u = heappop(hp)
            p = -p
            if u == end_node:
                return p
            for v, w in g[u]:
                np = p * w
                if np > prob[v]:
                    prob[v] = np
                    heappush(hp, (-np, v))
        return 0
# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.3]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[0.5]\n0\n2\n
# @lcpr case=end

#

