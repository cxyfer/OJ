# There is a grid with n + 2 horizontal bars and m + 2 vertical bars, and initially containing 1 x 1 unit cells.

# The bars are 1-indexed.

# You are given the two integers, n and m.

# You are also given two integer arrays: hBars and vBars.

# hBars contains distinct horizontal bars in the range [2, n + 1].
# vBars contains distinct vertical bars in the range [2, m + 1].
# You are allowed to remove bars that satisfy any of the following conditions:

# If it is a horizontal bar, it must correspond to a value in hBars.
# If it is a vertical bar, it must correspond to a value in vBars.
# Return an integer denoting the maximum area of a square-shaped hole in the grid after removing some bars (possibly none).

from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        maxH = 1
        i = 0
        while i < len(hBars) - 1:
            tmp = 1
            while i < len(hBars) - 1 and hBars[i] + 1 == hBars[i + 1]:
                tmp += 1
                i += 1
            maxH = max(maxH, tmp)
            i += 1
        maxV = 1
        i = 0
        while i < len(vBars) - 1:
            tmp = 1
            while i < len(vBars) - 1 and vBars[i] + 1 == vBars[i + 1]:
                tmp += 1
                i += 1
            maxV = max(maxV, tmp)
            i += 1
        maxWidth = min(maxH + 1, maxV + 1)
        return maxWidth * maxWidth
        

sol = Solution()

print(sol.maximizeSquareHoleArea(2, 4, [3, 2], [4, 2])) # 4
