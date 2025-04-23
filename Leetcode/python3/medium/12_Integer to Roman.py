#
# @lc app=leetcode.cn id=12 lang=python3
# @lcpr version=30204
#
# [12] 整数转罗马数字
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MP = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        base = 1000
        while num > 0:
            d, num = divmod(num, base)
            if d == 4:
                ans += MP[base] + MP[5 * base]
            elif d == 9:
                ans += MP[base] + MP[10 * base]
            else:
                if d > 4:
                    ans += MP[5 * base]
                    d -= 5
                ans += MP[base] * d
            base //= 10
        return ans
# @lc code=end

sol = Solution()
print(sol.intToRoman(3749))

#
# @lcpr case=start
# 3749\n
# @lcpr case=end

# @lcpr case=start
# 58\n
# @lcpr case=end

# @lcpr case=start
# 1994\n
# @lcpr case=end

#

