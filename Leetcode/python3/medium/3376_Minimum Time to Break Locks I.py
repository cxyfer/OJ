#
# @lc app=leetcode id=3376 lang=python3
# @lcpr version=30204
#
# [3376] Minimum Time to Break Locks I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMinimumTime(self, strength: list[int], K: int) -> int:
        n = len(strength)
        u = (1 << n) - 1
        @cache
        def dfs(s):
            if s == u:
                return 0
            X = 1 + s.bit_count() * K
            res = float('inf')
            for i in range(n):
                if s & (1 << i):
                    continue
                res = min(res, math.ceil(strength[i] / X) + dfs(s | (1 << i)))
            return res
        return dfs(0)
# @lc code=end



#
# @lcpr case=start
# [3,4,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,5,4]\n2\n
# @lcpr case=end

#

