# @algorithm @lc id=258 lang=python3 
# @title add-digits


from en.Python3.mod.preImport import *
# @test(38)=2
# @test(0)=0
class Solution:
    def addDigits(self, num: int) -> int:
        while(num >= 10):
            tmp = 0
            while(num > 0):
                tmp += num % 10
                num //= 10
            num = tmp
        return num