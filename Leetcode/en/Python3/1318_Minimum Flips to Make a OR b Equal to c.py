# @algorithm @lc id=1441 lang=python3 
# @title minimum-flips-to-make-a-or-b-equal-to-c


from en.Python3.mod.preImport import *
# @test(2,6,5)=3
# @test(4,2,7)=1
# @test(1,2,3)=0
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            ta, tb, tc = a & 1, b & 1, c & 1
            if (ta | tb) != tc:
                if tc == 0:
                    ans += ta + tb
                else:
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans