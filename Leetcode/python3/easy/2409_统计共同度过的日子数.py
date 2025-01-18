#
# @lc app=leetcode.cn id=2409 lang=python3
#
# [2409] 统计共同度过的日子数
#
from preImport import *
# @lc code=start

DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
DAYS_SUM = list(accumulate(DAYS, initial=0))

def parseDate(date: str) -> int:
    month, day = map(int, date.split('-'))
    return DAYS_SUM[month-1] + day

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        left = max(parseDate(arriveAlice), parseDate(arriveBob))
        right = min(parseDate(leaveAlice), parseDate(leaveBob))
        return max(right - left + 1, 0)

# @lc code=end

