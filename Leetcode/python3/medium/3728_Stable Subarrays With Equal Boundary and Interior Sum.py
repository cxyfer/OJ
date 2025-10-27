#
# @lc app=leetcode id=3728 lang=python3
#
# [3728] Stable Subarrays With Equal Boundary and Interior Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for r, x in enumerate(capacity):
            s += x
            ans += cnt[(s - x - x, x)]
            if r > 0:
                y = capacity[r - 1]
                cnt[(s - x, y)] += 1
        return ans
# @lc code=end

