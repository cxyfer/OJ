#
# @lc app=leetcode id=1331 lang=python3
# @lcpr version=30204
#
# [1331] Rank Transform of an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = dict()
        for i, k in enumerate(sorted(set(arr)), 1):
            rank[k] = i
        return [rank[x] for x in arr]
# @lc code=end



#
# @lcpr case=start
# [40,10,20,30]\n
# @lcpr case=end

# @lcpr case=start
# [100,100,100]\n
# @lcpr case=end

# @lcpr case=start
# [37,12,28,9,100,56,80,5,12]\n
# @lcpr case=end

#

