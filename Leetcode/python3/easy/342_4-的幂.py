#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.solve2(n)
    def solve1(self, n: int) -> bool: #
        while n > 1 and n % 4 == 0:
            n /= 4
        return n == 1
    def solve2(self, n: int) -> bool: # 是2的幂 且 二進位中1的位置在奇數位 (0xA = 1010)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0
    def solve3(self, n: int) -> bool: # 是2的幂 且 除以3餘1
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
# @lc code=end
sol = Solution()
print(sol.isPowerOfFour(16))
print(sol.isPowerOfFour(5))
print(sol.isPowerOfFour(1))