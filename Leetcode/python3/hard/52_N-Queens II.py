#
# @lc app=leetcode id=52 lang=python3
# @lcpr version=30204
#
# [52] N-Queens II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        pos = [-1] * n # 第 r 橫列 Q 在 pos[r] 列

        def check(r, c):
            for x in range(r): # 檢查前 r 橫列
                y = pos[x]
                if (r + c) == (x + y) or (r - c) == (x - y): # 在同一條斜線上
                    return False
            return True

        def dfs(r, used):
            if r == n:
                return 1
            res = 0
            for c in range(n):
                if (1 << c) & used:
                    continue
                if check(r, c):
                    pos[r] = c
                    res += dfs(r + 1, used | (1 << c))
            return res
        return dfs(0, 0)
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

