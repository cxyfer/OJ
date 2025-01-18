#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Digit DP
        # 2376. Count Special Integers  
        s = str(n)
        # 每個digit可以出現多次，不用mask處理集合
        @cache # memoize
        def cal(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s): # 填完所有位數，若此數字合法(is_num)，則返回1，否則返回0
                return int(is_num)
            res = 0 # 當前位數下，符合條件的特殊數字數量，初始為0
            if not is_num:  # 當還沒填合法數字時，可跳過當前digit
                res = cal(i + 1, False, False)
            lower = '0' if is_num else '1' # is_num
            upper = s[i] if is_limit else '9'  # is_limit
            for d in digits:  # 遍歷當前digit可填入的數字d
                if d > upper: break
                res += cal(i + 1, is_limit and d == upper, True) # 將此位填入 d，並更新 mask
            return res
        return cal(0, True, False)
# @lc code=end

