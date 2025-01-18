#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        for d in range(n):
            ans += (d // 7 + 1) + (d % 7)
        return ans
# @lc code=end

