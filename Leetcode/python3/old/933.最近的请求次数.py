3
#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#
from en.Python3.mod.preImport import *
# @lc code=start
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

