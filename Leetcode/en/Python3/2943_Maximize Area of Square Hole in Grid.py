# @algorithm @lc id=3214 lang=python3 
# @title maximize-area-of-square-hole-in-grid


from en.Python3.mod.preImport import *
# @test(2,1,[2,3],[2])=4
# @test(1,1,[2],[2])=4
# @test(2,3,[2,3],[2,3,4])=9
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def helper(bars):
            res = 1
            i = 0
            while i < len(bars) - 1:
                tmp = 1
                while i < len(bars) - 1 and bars[i] + 1 == bars[i + 1]:
                    tmp += 1
                    i += 1
                res = max(res, tmp)
                i += 1
            return res

        maxWidth = min(helper(hBars) + 1, helper(vBars) + 1)
        return pow(maxWidth, 2)