#
# @lc app=leetcode id=2872 lang=python3
# @lcpr version=30204
#
# [2872] Maximum Number of K-Divisible Components
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        def dfs(u, fa):
            nonlocal ans
            res = values[u]
            for v in g[u]:
                if v == fa:
                    continue
                res += dfs(v, u)
            if res % k == 0:  # 可以刪除 (u, fa) 這條邊
                ans += 1
            return res
        
        dfs(0, -1)
        return ans
# @lc code=end

sol = Solution()
print(sol.maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6)) # 2
print(sol.maxKDivisibleComponents(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3)) # 3

#
# @lcpr case=start
# 5\n[[0,2],[1,2],[1,3],[2,4]]\n[1,8,1,4,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]\n[3,0,6,1,5,2,1]\n3\n
# @lcpr case=end

#

