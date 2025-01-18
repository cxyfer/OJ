#
# @lc app=leetcode id=2928 lang=python3
# @lcpr version=30203
#
# [2928] Distribute Candies Among Children I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # return self.solve1(n, limit)
        # return self.solve2(n, limit)
        return self.solve3(n, limit)
    """
        1. Brute Force
    """
    def solve1(self, n: int, limit: int) -> int:
        ans = 0
        # for i in range(limit+1):
        for i in range(min(limit, n) + 1):
            # for j in range(limit+1):
            for j in range(min(limit, n - i) + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    ans += 1
        return ans
    """
        2. Optimized Brute Force
    """
    def solve2(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            mx = min(n - i, limit) # j 的上限
            mn = max(0, n - i - limit) # j 的下限
            ans += mx - mn + 1
        return ans
    """
        3. 排容原理
        - 所有方案數：
            H(3, n) = C(n+2, n) = C(n+2, 2)
        - 至少一人拿到超過 limit 個糖果的方案數：
            (先分(limit+1)給他，剩下的分給所有人)
            3 * H(3, n-(limit+1)) = 3 * C(n−(limit+1)+2, 2)
        - 至少兩人拿到超過 limit 個糖果的方案數：
            3 * C(n−2⋅(limit+1)+2, 2)
    """
    def solve3(self, n: int, limit: int) -> int:
        if n > 3 * limit: # 一定會有人拿到超過 limit 個糖果
            return 0
        ans = comb(n + 2, 2)
        if n >= (limit + 1): # 至少一人拿到超過 limit 個糖果
            ans -= 3 * comb(n - limit + 1, 2)
        if n >= 2 * (limit + 1): # 至少兩人拿到超過 limit 個糖果
            ans += 3 * comb(n - 2 * limit, 2)
        # if n >= 3 * (limit + 1): # 三人皆拿到超過 limit 個糖果
        #     ans -= comb(n - 3 * limit - 1, 2)
        return ans
# @lc code=end

sol = Solution()
print(sol.distributeCandies(1, 3)) # 3

#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#

