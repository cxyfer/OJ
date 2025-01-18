#
# @lc app=leetcode id=3038 lang=python3
# @lcpr version=30203
#
# [3038] Maximum Number of Operations With the Same Score I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Me
    2. 靈神，太優雅了
"""
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        return self.solve2(nums)
        # return self.solve3(nums)
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        target = nums[0] + nums[1]
        ans = 1
        for i in range(2, n, 2):
            if i + 1 < n and nums[i] + nums[i+1] == target:
                ans += 1
            else:
                break
        return ans
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        target = nums[0] + nums[1]
        for i in range(3, n, 2):
            if nums[i-1] + nums[i] != target:
                return i // 2
        return n // 2
    def solve3(self, nums: List[int]) -> int:
        return bisect_left(range(1, len(nums), 2), True, key= lambda x: any(nums[j-1] + nums[j] != nums[0] + nums[1] for j in range(3, x+1, 2)))
# @lc code=end

sol = Solution()
print(sol.maxOperations([3,2,1,4,5]))
print(sol.maxOperations([3,2,6,1,4]))

#
# @lcpr case=start
# [3,2,1,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,6,1,4]\n
# @lcpr case=end

#

