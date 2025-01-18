#
# @lc app=leetcode id=3067 lang=python3
# @lcpr version=30203
#
# [3067] Count Pairs of Connectable Servers in a Weighted Tree Network
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        DFS + 乘法原理
        Similar to 2867. Count Valid Paths in a Tree
    """
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1 # 注意樹中點的數量是邊數加一
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def dfs(u: int, fa: int, ps: int) -> int: # ps 是與根節點的距離
            res = 1 if ps % signalSpeed == 0 else 0 # 與根節點距離是 signalSpeed 的倍數的節點數
            for v, w in g[u]:
                if v == fa:
                    continue
                res += dfs(v, u, ps + w)
            return res
        ans = [0] * n

        for u, gu in enumerate(g): # 枚舉每個節點作為根節點
            pre = 0 # 前面子樹中符合條件的節點數
            for v, w in gu: 
                cur = dfs(v, u, w) # 以 v 為根的子樹，符合條件的節點數
                ans[u] += pre * cur # 乘法原理
                pre += cur
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]]\n3\n
# @lcpr case=end

#

