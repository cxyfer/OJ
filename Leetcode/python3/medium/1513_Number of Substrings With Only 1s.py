#
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
顯然符合條件的子字串一定是被 0 隔開的，因此我們可以將字串分割成多個全 1 子字串，然後對每個子字串計算其貢獻。
一個長度為 ln 的全 1 子字串，可以貢獻 ln * (ln + 1) // 2 個符合條件的子字串。

另一個思路是枚舉右端點，維護可能的左端點位置，即上一個 0 的位置後一位到右端點之間的任意位置。
這樣可以避免乘法可能有溢出的問題。
"""
# @lc code=start
MOD = int(1e9 + 7)

class Solution1:
    def numSub(self, s: str) -> int:
        # return sum(map(lambda x: x * (x + 1) // 2, [len(list(lst)) for c, lst in groupby(s) if c == '1'])) % MOD
        ans = 0
        for c, lst in groupby(s):
            if c == '0':
                continue
            ln = len(list(lst))
            ans += ln * (ln + 1) // 2
        return ans % MOD

class Solution2:
    def numSub(self, s: str) -> int:
        ans = 0
        last0 = -1
        for i, c in enumerate(s):  # 枚舉右端點
            if c == '0':
                last0 = i
            else:
                ans += i - last0  # [last0 + 1, i] 之間的任意位置都可以作為左端點
        return ans % MOD

# Solution = Solution1
Solution = Solution2
# @lc code=end

