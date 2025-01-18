# @algorithm @lc id=168 lang=python3 
# @title excel-sheet-column-title


from en.Python3.mod.preImport import *
# @test(1)="A"
# @test(28)="AB"
# @test(701)="ZY"
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ''
        while n > 0:
            n -= 1
            ans = chr((n) % 26 + ord('A')) + ans
            n //= 26
        return ans