#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#
import datetime
# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return self.solve1(day, month, year)
    """
        1. built-in function
    """
    def solve1(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year, month, day).strftime("%A")
    """
        Zeller's Congruence
    """
    def solve3(self, day: int, month: int, year: int) -> str:
        ANS_DICT = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month <= 2:
            year -= 1
            month += 12
        c = year // 100
        year %= 100
        return ANS_DICT[(year + (year // 4) + (c // 4) - 2 * c +  (13 * (month + 1)) // 5 + day - 1) % 7]
# @lc code=end

