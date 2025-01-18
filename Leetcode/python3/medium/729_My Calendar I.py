#
# @lc app=leetcode id=729 lang=python3
# @lcpr version=30204
#
# [729] My Calendar I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
from sortedcontainers import *

class MyCalendar1:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for st, ed in self.booked:
            if st < end and start < ed:
                return False
        self.booked.append((start, end))
        return True
    
class MyCalendar2:
    def __init__(self):
        self.booked = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.booked.bisect_left((start, end))
        if (idx > 0 and self.booked[idx-1][1] > start) or (idx < len(self.booked) and self.booked[idx][0] < end):
            return False
        self.booked.add((start, end))
        return True

# class MyCalendar(MyCalendar1):
class MyCalendar(MyCalendar2):
    pass

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end



