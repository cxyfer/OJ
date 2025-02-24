#
# @lc app=leetcode.cn id=2467 lang=python3
# @lcpr version=30204
#
# [2467] 树上最大得分和路径
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            
        bobTime = [float('inf')] * n

        def dfs_bob(u, fa, t):
            if u == 0:
                bobTime[u] = t
                return True
            for v in g[u]:
                if v == fa:
                    continue
                if dfs_bob(v, u, t + 1):
                    bobTime[u] = t
                    return True
            return False

        dfs_bob(bob, -1, 0)

        ans = -float('inf')
        def dfs_alice(u, fa, t, cur):
            nonlocal ans
            if t < bobTime[u]:
                cur += amount[u]
            elif t == bobTime[u]:
                cur += amount[u] // 2
            
            is_leaf = True
            for v in g[u]:
                if v == fa:
                    continue
                is_leaf = False
                dfs_alice(v, u, t + 1, cur)
            if is_leaf:
                ans = max(ans, cur)

        dfs_alice(0, -1, 0, 0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,1],[1,2],[1,3],[3,4]]\n3\n[-2,4,2,-4,6]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1]]\n1\n[-7280,2350]\n
# @lcpr case=end

#

