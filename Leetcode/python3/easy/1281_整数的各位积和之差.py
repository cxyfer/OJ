#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ans1, ans2 = 1, 0
        while(n > 0):
            d = n % 10
            ans1 *= d
            ans2 += d
            n //= 10
        return ans1 - ans2
# @lc code=end

