#
# @lc app=leetcode id=198 lang=python3
# @lcpr version=30201
#
# [198] House Robber
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 2) + nums[i], dfs(i - 1))  # rob / not rob

        return dfs(n - 1)


class Solution2:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i, x in enumerate(nums, start=2):
            f[i] = max(f[i - 2] + x, f[i - 1])  # rob / not rob
        return f[n + 1]


class Solution3:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f0 + x, f1)  # rob / not rob
        return f1


Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

