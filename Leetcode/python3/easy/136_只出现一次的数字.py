#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from preImport import *
# @lc code=start
class Solution:
    """
        XOR
        1. 0 ^ x = x
        2. x ^ x = 0
        3. XOR is commutative and associative
    """
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums: # 根據性質 2, 3，出現兩次的數字會被消除，又根據性質 1，最後剩下的就是只出現一次的數字
            ans ^= num
        return ans
# @lc code=end

