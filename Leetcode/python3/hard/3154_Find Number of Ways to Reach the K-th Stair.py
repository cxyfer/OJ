#
# @lc app=leetcode id=3154 lang=python3
# @lcpr version=30202
#
# [3154] Find Number of Ways to Reach the K-th Stair
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def f(x, j, flag): # x: current stair, j: 2^j, flag: can down
            if x < 0: return 0
            if x > k + 1: return 0 # 無法走到
            res = 1 if x == k else 0 # 走到了，但還能繼續走
            if flag:
                res += f(x-1, j, False) # 下1
            res += f(x + (1 << j), j+1, True)
            return res
        return f(1, 0, True)
# @lc code=end



#
# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

