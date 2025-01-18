#
# @lc app=leetcode.cn id=1318 lang=python3
#
# [1318] 或运算的最小翻转次数
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            ta, tb, tc = a & 1, b & 1, c & 1
            if (ta | tb) != tc:
                if tc == 0:
                    ans += ta + tb
                else:
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans
# @lc code=end
sol = Solution()
print(sol.minFlips(2, 6, 5)) # 3
print(sol.minFlips(4, 2, 7)) # 1
print(sol.minFlips(1, 2, 3)) # 0
