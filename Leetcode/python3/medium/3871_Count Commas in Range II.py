#
# @lc app=leetcode id=3871 lang=python3
#
# [3871] Count Commas in Range II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_D = 15
pow10 = [1] * (MAX_D + 1)
for i in range(1, MAX_D + 1):
    pow10[i] = pow10[i - 1] * 10

class Solution:
    def countCommas(self, n: int) -> int:
        k = (len(str(n)) - 1) // 3
        # return k * (n + 1) - 1000 * (pow10[3 * k] - 1) // 999
        ans = 0
        for d in range(1, k + 1):
            ans += n - pow10[3 * d] + 1
        return ans
# @lc code=end

sol = Solution()
print(sol.countCommas(999999999999998))