#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
反悔貪心
"""
# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # 按照 last_day 由小到大排序
        hp = []  # max heap
        cur = 0  # 已消耗天數
        for duration, last_day in courses:
            if cur + duration <= last_day:  # 沒有超過 last_day，可以上這門課程
                cur += duration
                heappush(hp, -duration)
                continue
            elif hp and duration < -hp[0]:  # 這門課程的時間比之前的最長時間要短，可以反悔
                cur -= -heapreplace(hp, -duration)
                cur += duration
        return len(hp)
# @lc code=end

