# @algorithm @lc id=1289 lang=python3 
# @title day-of-the-week


from en.Python3.mod.preImport import *
# @test(31,8,2019)="Saturday"
# @test(18,7,1999)="Sunday"
# @test(15,8,1993)="Sunday"
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