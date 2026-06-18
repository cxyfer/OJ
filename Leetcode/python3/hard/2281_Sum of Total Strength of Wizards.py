#
# @lc app=leetcode id=2281 lang=python3
#
# [2281] Sum of Total Strength of Wizards
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
貢獻法

首先可以改成枚舉最小值，考慮每個 strength[i] 作為最小值的貢獻，
可以令 L[i] 表示左側第一個 <= strength[i] 的位置，R[i] 表示右側第一個 < strength[i] 的最小位置，
則以 strength[i] 作為最小值的區間左端點可以為 [L[i] + 1, i]，右端點可以為 [i, R[i] - 1]。

而求 L[i] 和 R[i] 可以用 Monotonic Stack 來求解，
以求 R[i] 為例，可以維護一個單調遞增的 stack，當遇到一個元素 x 時，彈出所有 > x 的元素，並把彈出元素的 R 值設為當前元素的位置，
求 L[i] 的方法類似，只要倒過來遍歷並把 > x 改成 >= x 就行了。

至此可以解決一些比較簡單的類題。

---

但本題還需要對區間求和，可以用前綴和來表示區間和，那麼把以 strength[i] 作為最小值的區間都寫成前綴和的形式後，
可以得到左側的每個位置都會做為左端點 R[i] - i 次，右側的每個位置都會做為右端點 i - L[i] 次。

也就是說，如果我們可以知道 s 的區間和，就能在 O(1) 的時間計算這些區間的總和，從而得到以 strength[i] 作為最小值的貢獻，
也就是對前綴和再做一次前綴和即可。
"""
# @lc code=start
MOD = int(1e9) + 7

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)

        # L[i] 表示左側第一個 <= strength[i] 的位置
        # R[i] 表示右側第一個 < strength[i] 的最小位置
        L = [-1] * n
        R = [n] * n
        st = []
        for i, x in enumerate(strength):
            while st and x < strength[st[-1]]:
                R[st.pop()] = i
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            x = strength[i]
            while st and x <= strength[st[-1]]:
                L[st.pop()] = i
            st.append(i)

        s = list(accumulate(strength, initial=0))
        ss = list(accumulate(s, initial=0))

        ans = 0
        for i, x in enumerate(strength):
            # 以 strength[i] 作為最小值的區間左端點可以為 [L[i] + 1, i]，右端點可以為 [i, R[i] - 1]
            l, r = L[i] + 1, R[i] - 1
            a, b = i - l + 1, r - i + 1
            tot = a * (ss[r + 2] - ss[i + 1]) - b * (ss[i + 1] - ss[l])
            ans += tot * x % MOD
            ans %= MOD
        return ans
# @lc code=end

sol = Solution()
print(sol.totalStrength([1,3,1,2]))  # 44