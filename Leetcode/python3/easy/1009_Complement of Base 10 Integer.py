#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ ((1 << (max(n, 1).bit_length())) - 1)
# @lc code=end

sol = Solution()
print(sol.bitwiseComplement(5))  # 2
print(sol.bitwiseComplement(7))  # 0
print(sol.bitwiseComplement(10))  # 5
print(sol.bitwiseComplement(0))  # 1