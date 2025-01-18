# @algorithm @lc id=3055 lang=python3 
# @title maximum-odd-binary-number


from en.Python3.mod.preImport import *
# @test("010")="001"
# @test("0101")="1001"
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        cnt_1 = s.count('1')
        return '1' * (cnt_1 - 1) + '0' * (n - cnt_1) + '1'