#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
from functools import cache
class Solution:
    def countDigitOne(self, n: int) -> int:
        # Digit DP
        s = str(n)

        # cnt1: number of 1s in s[:i]
        @cache # memoize
        def cal(i: int, cnt1: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return cnt1
            res = 0 # 當前位數下，符合條件的特殊數字數量，初始為0
            if not is_num:  # 當還沒填合法數字時，可跳過當前digit
                res = cal(i + 1, cnt1, False, False)
            lower = 0 if is_num else 1  # is_num
            upper = int(s[i]) if is_limit else 9  # is_limit
            for d in range(lower, upper + 1):  # 遍歷當前digit可填入的數字d
                res += cal(i + 1, cnt1 + (d==1), is_limit and d == upper, True) # 將此位填入 d，若d==1則cnt1+=1
            return res
        return cal(0, 0, True, False)
# @lc code=end

