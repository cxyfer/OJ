# @algorithm @lc id=3017 lang=python3 
# @title number-of-beautiful-integers-in-the-range

from en.Python3.mod.preImport import *
# @test(10,20,3)=2
# @test(1,10,1)=1
# @test(5,5,2)=0

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        # Digit DP

        def sol(v): # from 0 to v
            s = str(v)
            # mod 表示 mod k 的值
            # diff 表示 奇數位和 與 偶數位和 的差
            @cache
            def cal(i: int, is_limit: bool, is_num: bool, mod:int, diff:int) -> int:
                if i == len(s): # 填完所有位數，若此數字合法，則返回1，否則返回0
                    return int(is_num) if mod == 0 and diff == 0 else 0
                res = 0 # 當前位數下，符合條件的特殊數字數量，初始為0
                if not is_num:  # 當還沒填合法數字時，可跳過當前digit
                    res = cal(i + 1, False, False, 0, 0)
                lower = 0 if is_num else 1  # is_num
                upper = int(s[i]) if is_limit else 9  # is_limit
                for d in range(lower, upper + 1):  # 遍歷當前digit可填入的數字d
                    new_diff = diff + 1 if d % 2 else diff - 1
                    res += cal(i + 1, is_limit and d == upper, True, (10 * mod + d) % k, new_diff) # 將此位填入 d，並更新 mask
                return res
            ans = cal(0, True, False, 0, 0)
            cal.cache_clear()
            return ans
        return sol(high) - sol(low - 1)
