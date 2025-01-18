#
# @lc app=leetcode id=1387 lang=python3
# @lcpr version=30204
#
# [1387] Sort Integers by The Power Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
@cache
def f(x: int) -> int:
    if x == 1:
        return 0
    return 1 + f(3 * x + 1) if x & 1 else 1 + f(x // 2)

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo, hi + 1), key=lambda x: (f(x), x))[k - 1]
# @lc code=end



#
# @lcpr case=start
# 12\n15\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n11\n4\n
# @lcpr case=end

#

