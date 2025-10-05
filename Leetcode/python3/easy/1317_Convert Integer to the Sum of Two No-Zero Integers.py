#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
延伸：如何讓 [a, b] 中的 a 最小？
"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        s = list(map(int, str(n)))
        m = len(s)

        @cache
        # flaga1: a 中是否已經出現 0，代表更高位都只能為前導 0
        # flaga2: a 中是否已經出現非 0 的數字，這是為了避免 a 全為 0
        # flagb1: b 中是否已經出現 0，代表更高位都只能為前導 0
        # flagb2: b 中是否已經出現非 0 的數字，這是為了避免 b 全為 0
        def dfs(i: int, borrow: int, flaga1: bool, flaga2: bool, flagb1: bool, flagb2: bool) -> Optional[str]:
            if i < 0:
                return "" if borrow == 0 else None
            res = None
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
                rest = dfs(i - 1, next_borrow, flaga1 or a_i == 0, flaga2 or a_i != 0, flagb1 or b_i == 0, flagb2 or b_i != 0)
                if rest is not None:
                   if res is None or (int(rest + str(a_i)) < int(res)):
                        res = rest + str(a_i)
            return res

        a = int(dfs(m - 1, 0, False, False, False, False))
        return [a, n - a]
# @lc code=end

sol = Solution()
# print(sol.getNoZeroIntegers(2))  # [1, 1]
# print(sol.getNoZeroIntegers(11))  # [2, 9]
# print(sol.getNoZeroIntegers(10000))  # [1, 9999]
# print(sol.getNoZeroIntegers(69))  # [1, 68]
# print(sol.getNoZeroIntegers(1010))  # [11, 999]
print(sol.getNoZeroIntegers(105))  # [6, 99]