#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        self.sz = size
        self.q = deque()
        self.s = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.s += val
        if len(self.q) > self.sz:
            self.s -= self.q.popleft()
        return self.s / len(self.q)
# @lc code=end

