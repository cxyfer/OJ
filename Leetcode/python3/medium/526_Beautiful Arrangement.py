#
# @lc app=leetcode id=526 lang=python3
# @lcpr version=30204
#
# [526] Beautiful Arrangement
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    狀態壓縮 DP ：排列型相鄰無關
    0 為未選擇，1 為已選擇
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        u = (1 << n) - 1
        @cache # Memoization
        def dfs(s: int) -> int:
            if s == u:
                return 1
            res = 0
            i = s.bit_count() + 1 # 當前選擇的數字下標
            for j in range(1, n + 1): 
                if (s >> (j - 1)) & 1 == 0: # 枚舉未選擇的數字 j
                    if i % j == 0 or j % i == 0: # perm[i] = j 滿足條件
                        res += dfs(s | (1 << (j - 1)))
            return res
        return dfs(0)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

