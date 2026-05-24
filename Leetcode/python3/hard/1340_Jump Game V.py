#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def dfs(i: int) -> int:
            res = 1
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dfs(j) + 1)
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dfs(j) + 1)
            return res

        return max(dfs(i) for i in range(n))
# @lc code=end

