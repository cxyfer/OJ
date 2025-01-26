#
# @lc app=leetcode id=3432 lang=python3
# @lcpr version=30204
#
# [3432] Count Partitions with Even Sum Difference
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # return 0 if sum(nums) % 2 else len(nums) - 1
        n = len(nums)
        ans = 0
        s = list(accumulate(nums))
        for i in range(n - 1):
            if abs(s[i] - (s[n-1] - s[i])) % 2 == 0:
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.countPartitions([10,10,3,7,6])) # 4

#
# @lcpr case=start
# [10,10,3,7,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,8]\n
# @lcpr case=end

#

