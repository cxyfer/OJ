#
# @lc app=leetcode id=2360 lang=python3
#
# [2360] Longest Cycle in a Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ind = [0] * n
        for u, v in enumerate(edges):
            if v == -1: continue
            ind[v] += 1

        q = deque(i for i, d in enumerate(ind) if d == 0)
        while q:
            u = q.popleft()
            v = edges[u]
            if v == -1: continue
            ind[v] -= 1
            if ind[v] == 0:
                q.append(v)

        ans = -1
        for u, d in enumerate(ind):
            if d == 0: continue
            cnt = 1
            v = edges[u]
            if v == -1: continue
            ind[u] = ind[v] = 0
            while v != u:
                cnt += 1
                v = edges[v]
                ind[v] = 0
            ans = max(ans, cnt)
        return ans
# @lc code=end

sol = Solution()
print(sol.longestCycle([2,-1,3,1])) # -1
print(sol.longestCycle([1,2,0,4,5,6,3,8,9,7])) # 4
