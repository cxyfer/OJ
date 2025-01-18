#
# @lc app=leetcode id=3180 lang=python3
# @lcpr version=30204
#
# [3180] Maximum Total Reward Using Operations I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        @cache
        def dfs(x: int) -> int:
            idx = bisect_right(rewardValues, x)
            ans = 0
            for v in rewardValues[idx:]:
                ans = max(ans, v + dfs(x + v))
            return ans
        return dfs(0)
# @lc code=end



#
# @lcpr case=start
# [1,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,6,4,3,2]\n
# @lcpr case=end

#

