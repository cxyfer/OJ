#
# @lc app=leetcode id=1140 lang=python3
# @lcpr version=30204
#
# [1140] Stone Game II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf = [0] * n # suffix sum
        suf[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + piles[i]
        @cache
        def dfs(i: int, m: int) -> int:
            if i + m * 2 >= n: # 自己可以全拿
                return suf[i]
            opponent = float("inf") # 枚舉對手可以拿的最小值
            for x in range(1, m * 2 + 1):
                opponent = min(opponent, dfs(i + x, max(m, x)))
            return suf[i] - opponent
        return dfs(0, 1)
# @lc code=end



#
# @lcpr case=start
# [2,7,9,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,100]\n
# @lcpr case=end

#

