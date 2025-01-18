# @algorithm @lc id=1070 lang=python3 
# @title convert-to-base-2


from en.Python3.mod.preImport import *
# @test(2)="110"
# @test(3)="111"
# @test(4)="100"
class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ""
        while n:
            q, r = divmod(n, -2)
            if r < 0:
                q += 1
                r += 2
            ans += str(r)
            n = q
        return ans[::-1] if ans else "0"