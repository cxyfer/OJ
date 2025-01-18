# @algorithm @lc id=1260 lang=python3 
# @title day-of-the-year


from en.Python3.mod.preImport import *
# @test("2019-01-09")=9
# @test("2019-02-10")=41
class Solution:
    DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
    S = list(accumulate(DAYS, initial=0)) # Prefix sum
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        isLeap = (y%4==0 and y%100!=0) or y%400==0 # 閏年
        return self.S[m-1] + d + (m>2 and isLeap)