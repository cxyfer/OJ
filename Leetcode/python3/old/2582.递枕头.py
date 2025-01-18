#
# @lc app=leetcode.cn id=2582 lang=python3
#
# [2582] 递枕头
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res = time % (2 * (n - 1))
        if res < n:
            return res + 1
        else:
            return 2 * (n - 1) - res + 1
# @lc code=end
sol = Solution()
print(sol.passThePillow(4, 5)) # 2
print(sol.passThePillow(4, 7)) # 2
print(sol.passThePillow(3, 2)) # 3


