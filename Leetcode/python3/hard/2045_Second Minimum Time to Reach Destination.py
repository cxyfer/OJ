#
# @lc app=leetcode id=2045 lang=python3
# @lcpr version=30204
#
# [2045] Second Minimum Time to Reach Destination
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 建圖
        g = [[] for _ in range(n)]
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)

        # BFS 維護最短路徑與次短路徑
        dis = [[float('inf')] * 2 for _ in range(n)] # (最短路徑, 次短路徑)
        dis[0][0] = 0
        q = deque([(0, 0)]) # (node, distance)
        while q: 
            u, d = q.popleft()
            switch = d // change # 紅綠燈的切換次數
            if switch & 1: # 當前是紅燈，需要等待切換為綠燈才能出發
                nd = (switch + 1) * change + time
            else: # 當前是綠燈，可以直接出發
                nd = d + time
            for v in g[u]:
                if nd < dis[v][0]: # new_d 比最短路徑小，就更新最短路徑
                    dis[v][0] = nd
                    q.append((v, nd))
                elif dis[v][0] < nd < dis[v][1]: # new_d 比最短路徑大又比次短路徑小，就更新次短路徑
                    dis[v][1] = nd
                    q.append((v, nd))
        return dis[n-1][1]
# @lc code=end

#
# @lcpr case=start
# 5\n[[1,2],[1,3],[1,4],[3,4],[4,5]]\n3\n5\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,2]]\n3\n2\n
# @lcpr case=end

#

