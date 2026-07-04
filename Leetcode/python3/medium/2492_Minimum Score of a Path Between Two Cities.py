#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in roads:
            u, v = u - 1, v - 1
            g[u].append((v, w))
            g[v].append((u, w))

        ans = inf
        q = deque([0])
        vis = [False] * n
        vis[0] = True
        while q:
            u = q.popleft()
            for v, w in g[u]:
                ans = min(ans, w)
                if not vis[v]:
                    q.append(v)
                    vis[v] = True
        return ans
# @lc code=end

"""
卡掉 Dijkstra 做法
https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/38161
"""
def hack():
    M = int(1e5)
    D = int(1e4)

    roads = []
    k = D - 1
    left_m = M - 3 * k
    for x in range(2, left_m + 2):
        roads.append([1, x, D])
    base = left_m + 2
    for i in range(1, k + 1):
        p = base + 2 * (i - 1)
        q = p + 1
        roads.append([1, p, D])
        roads.append([1, q, D])
        roads.append([p, q, D - i])
    n = 1 + left_m + 2 * k

    import os
    os.makedirs("hacks", exist_ok=True)
    with open("hacks/hack_2492.txt", "w") as f:
        f.write(f"{n}\n")
        f.write(str(roads))

# hack()