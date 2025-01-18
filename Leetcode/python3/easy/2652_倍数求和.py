#
# @lc app=leetcode.cn id=2652 lang=python3
#
# [2652] 倍数求和
#
from preImport import *
# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for num in range(2, n+1):
            for prime in [3, 5, 7]:
                if num % prime == 0:
                    ans += num
                    break
        return ans
# @lc code=end
sol = Solution()
print(sol.sumOfMultiples(7)) # 21
print(sol.sumOfMultiples(10)) # 40
