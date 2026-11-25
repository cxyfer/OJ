#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Weekly Contest 176 - Q4

逆向推導 + 最大堆 + 取模優化

由於陣列元素恆 >= 1，最後一次被修改的位置必定是當前陣列的最大值 x，
其修改前的值為 x - r（r 為其餘元素總和）。
為了避免極端測資（如 [1, 10^9]）逐次減 r 超時，透過取模一次跳過多步。

時間複雜度：O(n + log M * log n)，其中 M = max(target)
空間複雜度：O(n)（若原地建堆則額外空間為 O(1)）
"""
# @lc code=start
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        hp = target
        heapify_max(hp)

        while hp[0] > 1:
            x = hp[0]
            r = s - x  # 其餘元素的總和

            # r == 0：n = 1 且 x > 1，無法從 [1] 構造
            # x <= r：還原後的值 x - r <= 0，違反元素恆 >= 1
            if r == 0 or x <= r:
                return False

            # 連續減去 r 直到落入 [1, r] 區間
            # 如果 x % r == 0 則需要調整為 r
            y = (x - 1) % r + 1
            s += y - x
            heapreplace_max(hp, y)

        return True
# @lc code=end
sol = Solution()
print(sol.isPossible([9,3,5]))  # true