#
# @lc app=leetcode id=1870 lang=python3
# @lcpr version=30204
#
# [1870] Minimum Speed to Arrive on Time
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        if hour <= n - 1:
            return -1
        
        def check(v):
            t = 0
            for i in range(n):
                t += dist[i] / v
                if i < n - 1:
                    t = math.ceil(t)
            return t <= hour

        left, right = 1, 10**7
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # return left if left <= 10**7 else -1
        return left
# @lc code=end



#
# @lcpr case=start
# [1,3,2]\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2]\n2.7\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2]\n1.9\n
# @lcpr case=end

#

