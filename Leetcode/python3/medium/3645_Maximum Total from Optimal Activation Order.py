#
# @lc app=leetcode id=3645 lang=python3
#
# [3645] Maximum Total from Optimal Activation Order
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        g = defaultdict(list)
        for v, l in zip(value, limit):
            g[l].append(v)
        ans = 0
        for l, vals in g.items():
            vals.sort(reverse = True)
            ans += sum(vals[:l])
        return ans
# @lc code=end

