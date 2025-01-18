#
# @lc app=leetcode id=3206 lang=python3
# @lcpr version=30204
#
# [3206] Alternating Groups I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i, x in enumerate(colors):
            if x == colors[(i + 2) % n] and x != colors[(i + 1) % n]:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,0,1]\n
# @lcpr case=end

#

