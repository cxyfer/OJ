#
# @lc app=leetcode id=2218 lang=python3
# @lcpr version=30204
#
# [2218] Maximum Value of K Coins From Piles
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n:
                return 0
            res = dfs(i + 1, j)
            s = 0
            for k in range(min(j, len(piles[i]))):
                s += piles[i][k]
                res = max(res, dfs(i + 1, j - (k + 1)) + s)
            return res
        return dfs(0, k)
# @lc code=end



#
# @lcpr case=start
# [[1,100,3],[7,8,9]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]\n7\n
# @lcpr case=end

#

