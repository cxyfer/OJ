#
# @lc app=leetcode id=51 lang=python3
# @lcpr version=30204
#
# [51] N-Queens
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        path = [0] * n  # 第 i row 的 Q 在 第 path[i] col
        def check(x, y): 
            for i in range(x):  # 檢查前 x row
                j = path[i]
                if (x + y) == (i + j) or (x - y) == (i - j):  # 在同一條斜線上
                    return False
            return True

        def dfs(r: int, used: int):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in path])
                return
            for c in range(n):
                if (1 << c) & used:
                    continue
                if check(r, c):
                    path[r] = c
                    dfs(r + 1, used | (1 << c))
        dfs(0, 0)
        return ans
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

