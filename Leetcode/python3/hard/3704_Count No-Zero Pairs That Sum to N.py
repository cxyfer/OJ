#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Digit DP
和 1317. Convert Integer to the Sum of Two No-Zero Integers 中靈神給出的延伸題類似
只是把求最小的 a 改成求有多少對 a, b 滿足 a + b = n
"""
# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = list(map(int, str(n)))
        m = len(s)

        @cache
        # f[i] 表示 s[0...i] 中能獲得的最小的 a，且此時狀態定義如下：
        # borrow: 是否發生借位
        # flaga1: a 中是否已經出現 0，代表更高位都只能為前導 0
        # flaga2: a 中是否已經出現非 0 的數字，這是為了避免 a 全為 0
        # flagb1: b 中是否已經出現 0，代表更高位都只能為前導 0
        # flagb2: b 中是否已經出現非 0 的數字，這是為了避免 b 全為 0
        def dfs(i: int, borrow: int, flaga1: bool, flaga2: bool, flagb1: bool, flagb2: bool) -> int:
            if i < 0:
                return 1 if borrow == 0 else 0
            res = 0
            d = s[i] - borrow
            for a_i in (range((1 if not flaga2 else 0), 10) if not flaga1 else range(1)):
                b_i = d - a_i
                next_borrow = 0
                if b_i < 0:
                    b_i += 10
                    next_borrow = 1
                if flagb1 and b_i != 0:  # 此時 b_i 只能是前導 0
                    continue
                if not flagb2 and b_i == 0:  # 此時 b_i 只能是非 0
                    continue
                res += dfs(i - 1, next_borrow, flaga1 or a_i == 0, flaga2 or a_i != 0, flagb1 or b_i == 0, flagb2 or b_i != 0)
            return res

        return dfs(m - 1, 0, False, False, False, False)
# @lc code=end
sol = Solution()
print(sol.countNoZeroPairs(2))  # 1
print(sol.countNoZeroPairs(3))  # 2
print(sol.countNoZeroPairs(11))  # 8