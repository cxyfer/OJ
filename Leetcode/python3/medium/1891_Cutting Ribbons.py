#
# @lc app=leetcode id=1891 lang=python3
# @lcpr version=30204
#
# [1891] Cutting Ribbons
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def check(mid):
            return sum(x // mid for x in ribbons) >= k
        left, right = 1, max(ribbons)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end



#
# @lcpr case=start
# [9,7,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [7,5,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [5,7,9]\n22\n
# @lcpr case=end

#

