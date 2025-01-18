#
# @lc app=leetcode id=3296 lang=python3
# @lcpr version=30204
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(m: int) -> bool:
            tot = 0 # 降低的總高度
            for t in workerTimes: # 枚舉每個工人
                # 計算工人可以降低的高度
                """
                    t + 2t + 3t + ... + xt <= m
                    t * (x * (x + 1) // 2) <= m
                    x^2 + x - (2m / t) <= 0
                    x <= (-1 + sqrt(1 + 8 * m / t)) / 2
                """
                x = (-1 + math.isqrt(int(1 + 8 * m // t))) // 2
                tot += x
            return tot >= mountainHeight
        
        left, right = 0, int(1e18)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end



#
# @lcpr case=start
# 4\n[2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3,2,2,4]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[1]\n
# @lcpr case=end

#

