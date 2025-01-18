#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        nums = map(int, list(str(num)))
        return sum([1 for i in nums if i != 0 and num % i == 0])
# @lc code=end

