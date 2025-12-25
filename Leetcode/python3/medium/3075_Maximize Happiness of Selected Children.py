#
# @lc app=leetcode id=3075 lang=python3
# @lcpr version=30201
#
# [3075] Maximize Happiness of Selected Children
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Greedy + Sort 優先選最大的
"""
# @lc code=start
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        for i, x in enumerate(nlargest(k, happiness)):
            ans += max(0, x - i)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5]\n1\n
# @lcpr case=end

#

