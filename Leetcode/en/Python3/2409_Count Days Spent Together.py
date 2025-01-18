# @algorithm @lc id=2496 lang=python3 
# @title count-days-spent-together


from en.Python3.mod.preImport import *
# @test("08-15","08-18","08-16","08-19")=3
# @test("10-01","10-31","11-01","12-31")=0
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