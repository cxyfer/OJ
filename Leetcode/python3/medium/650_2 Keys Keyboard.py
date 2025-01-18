#
# @lc app=leetcode id=650 lang=python3
# @lcpr version=30204
#
# [650] 2 Keys Keyboard
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dfs(i, j): # 當前有 i 個字母，且剪貼版有 j 個字母
            if i > n:
                return float("inf")
            if i == n:
                return 0
            res = float("inf")
            if j > 0: # 貼上
                res = min(res, 1 + dfs(i + j, j))
            if i != j: # 複製
                res = min(res, 1 + dfs(i, i))
            return res
        return dfs(1, 0)
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

