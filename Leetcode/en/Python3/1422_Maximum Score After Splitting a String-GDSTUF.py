# @algorithm @lc id=1537 lang=python3 
# @title maximum-score-after-splitting-a-string


from en.Python3.mod.preImport import *
# @test("011101")=5
# @test("00111")=5
# @test("1111")=3
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        lcnt0, rcnt1 = 0, s.count('1')
        for ch in s[:-1]:
            if ch == '0':
                lcnt0 += 1
            else:
                rcnt1 -= 1
            ans = max(ans, lcnt0 + rcnt1)
        return ans