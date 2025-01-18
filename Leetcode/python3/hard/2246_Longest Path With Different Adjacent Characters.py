#
# @lc app=leetcode id=2246 lang=python3
# @lcpr version=30204
#
# [2246] Longest Path With Different Adjacent Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 0
        def dfs(u: int) -> int:
            nonlocal ans
            first = second = 0
            for v in g[u]:
                length = dfs(v)
                if s[u] == s[v]: # 注意這行要在 dfs 後面，因為子樹中可能會有更長的路徑
                    continue
                if length > first:
                    first, second = length, first
                elif length > second:
                    second = length
            ans = max(ans, first + second + 1)
            return first + 1
        dfs(0)
        return ans
# @lc code=end
sol = Solution()
print(sol.longestPath([-1,0,1], "aab")) # 2

#
# @lcpr case=start
# [-1,0,0,1,1,2]\n"abacbe"\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,0,0]\n"aabc"\n
# @lcpr case=end

#

