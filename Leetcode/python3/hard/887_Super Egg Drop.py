#
# @lc app=leetcode id=887 lang=python3
# @lcpr version=30204
#
# [887] Super Egg Drop
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def f(k: int, n: int) -> int:
            if k == 1:
                return n
            if n == 0:
                return 0
            res = float('inf')
            # for i in range(1, n + 1):
            #     res = min(res, max(f(k - 1, i - 1), f(k, n - i)) + 1)
            left, right = 1, n
            while left <= right:
                mid = (left + right) // 2
                broken = f(k - 1, mid - 1) # 遞增函數
                not_broken = f(k, n - mid) # 遞減函數
                if broken > not_broken:
                    right = mid - 1
                elif broken < not_broken:
                    left = mid + 1
                else:
                    return broken + 1
            for x in [left, right]:
                res = min(res, max(f(k - 1, x - 1), f(k, n - x)) + 1)
            return res
        return f(k, n)
# @lc code=end

sol = Solution()
print(sol.superEggDrop(1, 2))
print(sol.superEggDrop(2, 6))
print(sol.superEggDrop(3, 14))
print(sol.superEggDrop(2, 2)) # 2

#
# @lcpr case=start
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 2\n6\n
# @lcpr case=end

# @lcpr case=start
# 3\n14\n
# @lcpr case=end

#

