#
# @lc app=leetcode id=3740 lang=python3
#
# [3740] Minimum Distance Between Three Equal Elements I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        pos = [[] for _ in range(n + 1)]
        for i, x in enumerate(nums):
            if len(pos[x]) >= 2:
                ans = min(ans, (i - pos[x][-2]) << 1)
            pos[x].append(i)
        return ans if ans < float('inf') else -1
# @lc code=end

