#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.w = w
        self.s = list(accumulate(w))

    def pickIndex(self) -> int:
        # return choices(range(self.n), weights=self.w)[0]
        rnd = randint(1, self.s[-1])
        return bisect_left(self.s, rnd)

# @lc code=end
obj = Solution([1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())


