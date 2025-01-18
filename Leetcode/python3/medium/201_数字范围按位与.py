#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # return self.solve1(left, right) 
        return self.solve2(left, right)
    def solve1(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
    def solve2(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1) # 消除最低位的1
        return right
# @lc code=end

