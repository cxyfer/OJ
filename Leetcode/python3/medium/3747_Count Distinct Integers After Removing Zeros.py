#
# @lc app=leetcode id=3747 lang=python3
#
# [3747] Count Distinct Integers After Removing Zeros
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
求 [1, n] 中不包含 0 的數的個數。

令 m 為 n 的位數，則在 k 位數 (k < m) 的數中，有 9 ^ (k - 1) 個。
對於 m 位數，我們可以用限制前綴的辦法來計算：
- 例如對於 45678，我們可以先計算 1XXXX~3XXXX 的個數，有 3 * 9 ^ 4 個；然後再計算 41XXX~44XXX 的個數，有 3 * 9 ^ 3 個，依此類推。
- 注意遇到 0 時，後面的數字都無法選擇。
- 另外上述方法中會忽略 n 本身，因此若 n 不包含 0，則最後需要 +1。
"""
# @lc code=start
class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)

        # 9 + 9^2 + ... + 9^(m-1) = (9^m - 9) / 8
        pow9 = 9 ** m
        ans = (pow9 - 9) // 8 

        for d in map(int, s):
            if d == 0:
                break
            pow9 //= 9
            ans += (d - 1) * pow9
        else:
            ans += 1

        return ans
# @lc code=end

