#
# @lc app=leetcode.cn id=2226 lang=python3
# @lcpr version=30204
#
# [2226] 每个小孩最多能分到多少糖果
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(m):
            return sum(c // m for c in candies) >= k
        
        left, right = 1, min(max(candies), sum(candies) // k)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end

sol = Solution()
print(sol.maximumCandies([2,5], 11))  # 0

#
# @lcpr case=start
# [5,8,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,5]\n11\n
# @lcpr case=end

#

