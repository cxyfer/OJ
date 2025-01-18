# @algorithm @lc id=6 lang=python3 
# @title zigzag-conversion


from en.Python3.mod.preImport import *
# @test("PAYPALISHIRING",3)="PAHNAPLSIIGYIR"
# @test("PAYPALISHIRING",4)="PINALSIGYAHRPI"
# @test("A",1)="A"
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        n = len(s)
        ans = ["" for i in range(numRows)]
        idx = 0
        dir = 1
        for ch in s:
            ans[idx] += ch
            if idx == 0:
                dir = 1
            elif idx == numRows - 1:
                dir = -1
            idx += dir
        return "".join(ans)