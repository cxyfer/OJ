#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lcpr-template-start
import time

from preImport import *


# @lcpr-template-end
# @lc code=start
class TimeMap:
    def __init__(self):
        self.ts = defaultdict(list)
        self.ws = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts[key].append(timestamp)
        self.ws[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.ts[key], timestamp)
        return self.ws[key][idx - 1] if idx > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
