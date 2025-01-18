#
# @lc app=leetcode id=3364 lang=python3
# @lcpr version=30204
#
# [3364] Minimum Positive Sum Subarray 
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = float('inf')
        for ln in range(l, r + 1):
            for i in range(n - ln + 1):
                cur = s[i + ln] - s[i]
                if cur > 0:
                    ans = min(ans, cur)
        return ans if ans != float('inf') else -1
# @lc code=end

sol = Solution()
print(sol.minimumSumSubarray([3, -2, 1, 4], 2, 3))  # 1
print(sol.minimumSumSubarray([-2, 2, -3, 1], 2, 3))  # -1
print(sol.minimumSumSubarray([1, 2, 3, 4], 2, 4))  # 3

#
# @lcpr case=start
# [3, -2, 1, 4]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [-2, 2, -3, 1]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3, 4]\n2\n4\n
# @lcpr case=end

#

