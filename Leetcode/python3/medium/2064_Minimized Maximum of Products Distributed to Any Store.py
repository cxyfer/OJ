#
# @lc app=leetcode id=2064 lang=python3
# @lcpr version=30204
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(x):
            # return sum(math.ceil(q / x) for q in quantities) <= n
            return sum((q + x - 1) // x for q in quantities) <= n
        left, right = 1, max(quantities)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

sol = Solution()
print(sol.minimizedMaximum(2, [5,7])) # 7

#
# @lcpr case=start
# 6\n[11,6]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[15,10,10]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[100000]\n
# @lcpr case=end

#

