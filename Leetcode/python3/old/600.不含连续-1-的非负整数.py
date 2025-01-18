#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
# 给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。

from functools import cache
# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        # Digit DP
        s = format(n, 'b') # 將 n 轉為二進制字串
        # pre1: whether the previous digit is 1
        @cache # memoize
        def cal(i: int, pre1: bool, is_limit: bool) -> int:
            if i == len(s): # 填完所有位數
                return 1
            upper = int(s[i]) if is_limit else 1  # is_limit
            res = cal(i + 1, False, is_limit and upper == 0) # 當前位數填0
            if not pre1 and upper == 1: # 若前一位是0，且當前位可以填入1
                res += cal(i + 1, True, is_limit and upper == 1) # 當前位數填1
            return res
        return cal(0, False, True)
# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    sol.findIntegers(5)

