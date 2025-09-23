#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for x, y in zip_longest(map(int, version1.split('.')), map(int, version2.split('.')), fillvalue=0):
            if x > y:
                return 1
            elif x < y:
                return -1
        return 0
# @lc code=end

