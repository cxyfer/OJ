#
# @lc app=leetcode.cn id=2646 lang=python3
#
# [2646] 最小化旅行的价格总和
#
from preImport import *
# @lc code=start
class Solution:
    """
        樹形DP + LCA，兩次DFS
        1. 這題分成兩個部分，根據起點和終點，計算每個城市經過的次數
        2. 再來就是用樹形DP判斷每個城市的選或不選
    """
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 第一次DFS，計算每個城市在樹上的父節點和深度
        fat = [0] * n # 每個節點的父節點
        dep = [0] * n # 以0為根，每個節點的深度

        def dfs1(u, fa):
            fat[u] = fa
            if fa != -1: # 0為根，沒有父節點，但因為python的索引特性其實不影響，只是深度變成從1開始
                dep[u] = dep[fa] + 1
            for v in g[u]:
                if v != fa:
                    dfs1(v, u)
        dfs1(0, -1)
        
        # 根據trips，計算每個城市經過的次數，最近公共祖先
        cnt = [0] * n
        for u, v in trips:
            if dep[u] < dep[v]: # 保證u在的深度>=v在的深度
                u, v = v, u
            while dep[u] > dep[v]: # u一直往上找，直到深度相同
                cnt[u] += 1
                u = fat[u]
            while u != v: # 深度相同時仍未相遇，繼續一起往上找公共祖先
                cnt[u] += 1
                cnt[v] += 1
                u = fat[u]
                v = fat[v]
            cnt[u] += 1 # 最後相遇的點，也要計算

        # 樹形DP，計算每個城市的選或不選
        # dp[i][0] 表示不選i的最小花費
        # dp[i][1] 表示選i的最小花費
        # dp[i][0] = price[cur] * cnt[cur] + sum(max(dp[to][0], dp[to][1]))
        # dp[i][1] = price[cur] // 2 * cnt[cur] + sum(dp[to][0])
        dp = [[float('inf')] * 2 for _ in range(n)]

        def dfs2(u, fa):
            dp[u][0] = price[u] * cnt[u] # 不選i，則i的花費為price[i]*cnt[i]
            dp[u][1] = price[u] // 2 * cnt[u] # 選i，則i的花費為price[i]//2*cnt[i]
            for v in g[u]:
                if v != fa:
                    dfs2(v, u)
                    dp[u][1] += dp[v][0] # 選u，則v必不選，所以取dp[v][0]
                    dp[u][0] += min(dp[v][0], dp[v][1]) # 不選u，則v可選可不選，所以取min(dp[v][0], dp[v][1])
        dfs2(0, -1)
        return min(dp[0])
# @lc code=end

sol = Solution()
print(sol.minimumTotalPrice(4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]])) # 23
print(sol.minimumTotalPrice(2, [[0,1]], [2,2], [[0,0]])) # 1