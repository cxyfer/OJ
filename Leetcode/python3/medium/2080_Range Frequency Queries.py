#
# @lc app=leetcode id=2080 lang=python3
# @lcpr version=30204
#
# [2080] Range Frequency Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        p = self.pos[value]
        return bisect_right(p, right) - bisect_left(p, left)

# @lc code=end



