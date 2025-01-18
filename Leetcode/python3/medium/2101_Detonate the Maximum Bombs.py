#
# @lc app=leetcode id=2101 lang=python3
# @lcpr version=30204
#
# [2101] Detonate the Maximum Bombs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. DFS
    2. Bitset + Floyd-Warshall
"""
class Solution1:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i == j:
                    continue
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    g[i].append(j)

        def dfs(i: int) -> int:
            vis[i] = True
            res = 1
            for j in g[i]:
                if not vis[j]:
                    res += dfs(j)
            return res

        ans = 0
        for i in range(n):
            vis = [False] * n
            ans = max(ans, dfs(i))
        return ans

class Solution2:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        dp = [0] * (n) # dp[i] 表示以 i 為起點可到達的節點集合
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    dp[i] |= 1 << j
        for k in range(n): # 枚舉中間點
            for i in range(n):
                if dp[i] & (1 << k): # 如果 i 可以到達 k ，則 i 可以到達 k 可到達的所有點 
                    dp[i] |= dp[k]
        return max(i.bit_count() for i in dp)

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [[2,1,3],[6,1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,5],[10,10,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]\n
# @lcpr case=end

#

