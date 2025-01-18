# @algorithm @lc id=600 lang=python3 
# @title non-negative-integers-without-consecutive-ones

from en.Python3.mod.preImport import *
# @test(5)=5
# @test(1)=2
# @test(2)=3
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
        