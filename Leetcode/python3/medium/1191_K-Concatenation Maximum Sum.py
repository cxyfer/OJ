#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        tot = sum(arr)
        A = arr * min(2, k)
        ans = f = 0
        for x in A:
            f = max(x, f + x)
            ans = max(ans, f)
        if tot >= 0 and k > 1:
            return (ans + (k - 2) * tot) % MOD
        else:
            return ans % MOD
# @lc code=end

sol = Solution()
print(sol.kConcatenationMaxSum([4,-10,-2,-3,4], 1))  # 4
print(sol.kConcatenationMaxSum([1,2], 1))  # 3