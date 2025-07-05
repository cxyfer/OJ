#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([k for k, v in Counter(arr).items() if k == v], default=-1)
# @lc code=end

