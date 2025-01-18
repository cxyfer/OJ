#
# @lc app=leetcode.cn id=3079 lang=python3
#
# [3079] 求出加密整数的和
#
from preImport import *
# @lc code=start
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def calc(x):
            mx, d = 0, 0
            while x > 0:
                t = x % 10
                mx = max(mx, t)
                x //= 10
                d += 1
            return int(str(mx) * d)
        ans = 0
        for x in nums:
            ans += calc(x)
        return ans
# @lc code=end
sol = Solution()
print(sol.sumOfEncryptedInt([10,21,31])) # 66
