# @algorithm @lc id=2650 lang=python3 
# @title split-with-minimum-sum


from en.Python3.mod.preImport import *
# @test(4325)=59
# @test(687)=75
class Solution:
    def splitNum(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        digits.sort(reverse=True)
        ans = 0
        cur = 1
        for i, d in enumerate(digits):
            if i % 2 == 0 and i != 0:
                cur *= 10
            ans += cur * d
        return ans

        