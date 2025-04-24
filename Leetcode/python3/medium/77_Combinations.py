#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(combinations(range(1, n + 1), k))
        ans = []
        path = []
        def dfs(i):
            if len(path) == k:
                ans.append(path[:])
                return
            for j in range(i, n + 1):
                path.append(j)
                dfs(j + 1)
                path.pop()
        dfs(1)
        return ans
# @lc code=end

