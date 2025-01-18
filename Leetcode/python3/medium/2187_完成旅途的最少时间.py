#
# @lc app=leetcode.cn id=2187 lang=python3
#
# [2187] 完成旅途的最少时间
#
from preImport import *
# @lc code=start
class Solution:
    """
        Binary search
        對答案 t 進行二分搜尋
    """
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips

        def check(t): # t 時間內是否能完成 totalTrips 次旅程
            s = 0
            for x in time:
                s += t // x
            return s >= totalTrips
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

