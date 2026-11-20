#
# @lc app=leetcode id=3041 lang=python3
#
# [3041] Maximize Consecutive Elements in an Array After Modification
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-endSP
# @lc code=start
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = defaultdict(int)
        for x in nums:
            f[x + 1] = f[x] + 1
            f[x] = f[x - 1] + 1
        return max(f.values())
# @lc code=end

