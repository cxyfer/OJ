# @algorithm @lc id=969 lang=python3 
# @title number-of-recent-calls

from en.Python3.mod.preImport import *

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)