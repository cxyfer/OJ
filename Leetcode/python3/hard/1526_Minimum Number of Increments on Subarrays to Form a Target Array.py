#
# @lc app=leetcode id=1526 lang=python3
#
# [1526] Minimum Number of Increments on Subarrays to Form a Target Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. DP
令 f[i] 表示將 initial[0...i] 變成 target[0...i] 所需的最小操作數，則
- 如果 target[i] <= target[i - 1]，則當前位置不需操
- 如果 target[i] > target[i - 1]，則當前位置還需要操作 (target[i] - target[i - 1]) 次
得到遞迴式 f[i] = f[i - 1] + max(0, target[i] - target[i - 1])

2. 差分 + 貪心
注意到題目中有區間增減的操作，可以轉換為在差分陣列上操作，
則所求等同於把一個全 0 陣列變為 target 的差分陣列 d 所需的最小操作數。
- 若在差分陣列的後綴上操作，則可以在一個位置上 +1
- 若在非後綴上操作，則可以在一個位置 +1，之後的一個位置 -1。

為了最小化操作次數，應該盡量先操作兩個位置的加一減一，最後才使用一個位置的加一。
而兩種操作都可以使一個位置加一，因此最少操作次數等同於差分陣列中正數的和。

正確性證明：
- 因為題目保證 target[i] > 0，因此不會出現差分陣列中負數的和 > 正數的和的情況。

P.S. 其實兩種解法的寫法可以是完全一樣的，區別在要從哪個角度切入。
"""
# @lc code=start
class Solution1:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        f = [0] * n
        f[0] = target[0]
        for i, (x, y) in enumerate(pairwise(target), 1):
            if y <= x:
                f[i] = f[i - 1]
            else:
                f[i] = f[i - 1] + (y - x)
        return f[-1]

class Solution2:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for (x, y) in pairwise(target):
            ans += max(0, y - x)
        return ans

Solution = Solution2
# @lc code=end

