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
只是把求最小的 a 改成求有多少對 a, b 滿足 a + b = n 。

而相比 1317 ，本題可以事後再根據 n 是否包含 0 來扣除 (0, n) 和 (n, 0) 這兩種情況，可以少兩個狀態。
"""
# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = list(map(int, str(n)))
        m = len(s)

        @cache
        # f[i] 表示 s[0...i] 中能獲得的最小的 a，且此時狀態定義如下：
        # borrow: 是否發生借位
        # has_zero_a: a 中是否已經出現 0，代表更高位都只能為前導 0
        # has_zero_b: b 中是否已經出現 0，代表更高位都只能為前導 0
        def dfs(i: int, borrow: bool, has_zero_a: bool, has_zero_b: bool) -> int:
            if i < 0:
                return 1 if borrow == 0 else 0
            res = 0
            d = s[i] - borrow
            for a_i in (range(10) if not has_zero_a else range(1)):
                b_i = d - a_i
                b_i += 10 if (next_borrow := b_i < 0) else 0
                if has_zero_b and b_i != 0:  # 此時 b_i 只能是前導 0
                    continue
                res += dfs(i - 1, next_borrow, has_zero_a or a_i == 0, has_zero_b or b_i == 0)
            return res
        return dfs(m - 1, False, False, False) - (2 if 0 not in s else 0)  # 減去 (0, n) 和 (n, 0) 這兩種情況
# @lc code=end
sol = Solution()
print(sol.countNoZeroPairs(2))  # 1
print(sol.countNoZeroPairs(3))  # 2
print(sol.countNoZeroPairs(11))  # 8
print(sol.countNoZeroPairs(10))  # 9