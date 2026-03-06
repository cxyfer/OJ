#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def checkOnesSegment(self, s: str) -> bool:
        return sum(x != y for x, y in pairwise(s)) <= 1

class Solution2:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s

# Solution = Solution1
Solution = Solution2
# @lc code=end

