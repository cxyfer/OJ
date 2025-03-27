#
# @lc app=leetcode id=3483 lang=python3
#
# [3483] Unique 3-Digit Even Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()
        for (x, y, z) in permutations(digits, 3):
            if x == 0 or z & 1: continue
            ans.add(x * 100 + y * 10 + z)
        return len(ans)
# @lc code=end

