#
# @lc app=leetcode id=575 lang=python3
# @lcpr version=30203
#
# [575] Distribute Candies
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # return min(len(candyType)//2, len(set(candyType)))
        n = len(candyType)
        st = set(candyType)
        return min(n//2, len(st))
# @lc code=end



#
# @lcpr case=start
# [1,1,2,2,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,6,6]\n
# @lcpr case=end

#

