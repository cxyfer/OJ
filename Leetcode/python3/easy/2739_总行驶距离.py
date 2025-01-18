#
# @lc app=leetcode.cn id=2739 lang=python3
#
# [2739] 总行驶距离
#

# @lc code=start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5 and additionalTank:
            q, r = divmod(mainTank, 5)
            ans += 5 * q * 10
            used = min(q, additionalTank)
            mainTank = r + used
            additionalTank -= used
        ans += mainTank * 10
        return ans

# @lc code=end

