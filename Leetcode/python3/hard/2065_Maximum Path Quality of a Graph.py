#
# @lc app=leetcode id=2065 lang=python3
# @lcpr version=30204
#
# [2065] Maximum Path Quality of a Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))

        ans = 0
        visited = [False] * n

        def dfs(u: int, time: int, quality: int) -> None:
            if u == 0: # 回到起點，需要更新答案，但還可以繼續往下走，不用 return
                nonlocal ans
                ans = max(ans, quality)
            for v, t in g[u]:
                if time + t > maxTime:
                    continue
                if not visited[v]: # 沒有走過，可以獲得 value
                    visited[v] = True
                    dfs(v, time + t, quality + values[v])
                    visited[v] = False
                else: # 走過了，還是可以繼續往下走，但是不會獲得 value
                    dfs(v, time + t, quality)

        visited[0] = True
        dfs(0, 0, values[0])
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,32,10,43]\n[[0,1,10],[1,2,15],[0,3,10]]\n49\n
# @lcpr case=end

# @lcpr case=start
# [5,10,15,20]\n[[0,1,10],[1,2,10],[0,3,10]]\n30\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n[[0,1,10],[1,2,11],[2,3,12],[1,3,13]]\n50\n
# @lcpr case=end

#

