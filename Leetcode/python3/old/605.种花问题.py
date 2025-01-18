#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur = 1
        for flower in flowerbed:
            if flower == 1:
                if cur != 0:
                    n -= (cur - 1) // 2
                cur = 0
            else:
                cur += 1
        if flowerbed[-1] == 0:
            n -= cur // 2
        return n <= 0
# @lc code=end

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1],1))

