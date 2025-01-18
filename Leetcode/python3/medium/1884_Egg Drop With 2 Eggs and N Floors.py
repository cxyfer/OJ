#
# @lc app=leetcode id=1884 lang=python3
# @lcpr version=30204
#
# [1884] Egg Drop With 2 Eggs and N Floors
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            res = float('inf')
            for j in range(1, i + 1):
                res = min(res, max(j, dfs(i - j) + 1)) # 碎了 / 沒碎
            return res
        return dfs(n)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 100\n
# @lcpr case=end

#

