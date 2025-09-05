#
# @lc app=leetcode id=2749 lang=python3
#
# [2749] Minimum Operations to Make the Integer Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
找出一個最小的 k，使得 x = num1 - k * num2 可以被表示成恰好 k 個 2 的冪的和

而一個非負整數 x 一定可以可以寫成 x * 2^0 ，因此最多可以寫成 x 個 2 的冪的和；
最少可以由 x 的二進制表示中 1 的個數個 2 的冪的和組成，即 x.bit_count() 個 2 的冪的和。
由於 2^d = 2^(d-1) + 2^(d-1)，因此若 x 可以被表示成 k 個 2 的冪的和，則 x 也可以被表示成 k+1 個 2 的冪的和，
故 k 的有效範圍為 [x.bit_count(), x]。

而 k 要枚舉到多少，可以由 num2 的正負號來決定：
- 若 num2 為正，則 x.bit_count() 的最大值為 log2(num1) = 30，故若 k 有解則最多枚舉到 30；
- 若 num2 為負，則考慮以下構造方式可以使 k 最大，
  - 使得過程中出現的每個 x 都至少有 d 個 1，且之後在減 num2 的過程中，盡可能地不更動低位的 1。
  - 範圍內有最多個 1 的數為 1 << 30 - 1，即 d = 30，
  - 當 k < 30 時，一定無解；而當 k = 31 時，x.bit_count() = 29 + 5 = 34，也無解；但當 k = 32 時，x.bit_count() = 29 + 1 = 30，有解。
  - 故 k 最大枚舉到 32 即可。
"""
# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 33):
            x = num1 - k * num2
            if x.bit_count() <= k <= x:
                return k
        return -1
# @lc code=end
num1 = (1 << 29) - 1
num2 = -(1 << 29)
print(num1, num2)
sol = Solution()
print(sol.makeTheIntegerZero(num1, num2))