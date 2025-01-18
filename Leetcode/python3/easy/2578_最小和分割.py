#
# @lc app=leetcode.cn id=2578 lang=python3
#
# [2578] 最小和分割
#

# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        digits.sort(reverse=True)
        ans = 0
        cur = 1
        for i, d in enumerate(digits):
            if i % 2 == 0 and i != 0:
                cur *= 10
            ans += cur * d
        return ans
# @lc code=end
sol = Solution()
print(sol.splitNum(4325)) # 59
print(sol.splitNum(687)) # 75


