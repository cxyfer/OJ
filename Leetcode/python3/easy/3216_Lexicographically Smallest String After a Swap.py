#
# @lc app=leetcode id=3216 lang=python3
# @lcpr version=30204
#
# [3216] Lexicographically Smallest String After a Swap
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getSmallestString(self, s: str) -> str:
        lst = list(map(int, s))
        for i, (x, y) in enumerate(pairwise(lst)):
            if x & 1 == y & 1 and x > y:
                lst[i], lst[i + 1] = y, x
                break
        return ''.join(map(str, lst))
# @lc code=end



#
# @lcpr case=start
# "45320"\n
# @lcpr case=end

# @lcpr case=start
# "001"\n
# @lcpr case=end

#

