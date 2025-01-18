#
# @lc app=leetcode id=933 lang=python3
# @lcpr version=30201
#
# [933] Number of Recent Calls
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end



