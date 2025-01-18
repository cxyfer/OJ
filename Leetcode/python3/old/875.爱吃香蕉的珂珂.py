#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        left, right = 1, max(piles)

        def check(k):
            tmp = 0
            for i in piles:
                tmp += math.ceil(i/k)
            return tmp <= h
        
        while (left < right):
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

sol = Solution()
print(sol.minEatingSpeed([312884470], 968709470))