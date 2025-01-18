#
# @lc app=leetcode id=3373 lang=python3
# @lcpr version=30204
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(m)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        
        # 以圖 g 中的 u 為根節點，計算與 u 距離為偶數和奇數的節點數
        def bfs(u, g):
            q = deque([(u, 0)])
            dist = [float('inf')] * len(g)
            dist[u] = 0
            cnt = [0, 0] # cnt[0] 是距離為偶數的節點數，cnt[1] 是距離為奇數的節點數
            while q:
                u, d = q.popleft()
                cnt[d & 1] += 1
                for v in g[u]:
                    nd = d + 1
                    if nd < dist[v]:
                        dist[v] = nd
                        q.append((v, nd))
            return dist, cnt

        dist1, cnt1 = bfs(0, g1)
        dist2, cnt2 = bfs(0, g2)
        mx2 = max(cnt2) # 取 g2 中兩個部分的最大值

        ans = [-1] * n
        for x in range(n):
            if dist1[x] & 1: # 在 g1 中是屬於奇數點
                ans[x] = cnt1[1] + mx2
            else: # 在 g1 中是屬於偶數點
                ans[x] = cnt1[0] + mx2
        return ans
# @lc code=end
sol = Solution()
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
print(sol.maxTargetNodes(edges1, edges2)) # [8,7,7,8,8]
#
# @lcpr case=start
# [[0,1],[0,2],[2,3],[2,4]]\n[[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,2],[0,3],[0,4]]\n[[0,1],[1,2],[2,3]]\n
# @lcpr case=end

#

