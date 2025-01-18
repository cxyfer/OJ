#
# @lc app=leetcode id=945 lang=python3
# @lcpr version=30203
#
# [945] Minimum Increment to Make Array Unique
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        # return self.solve2a(nums)
        return self.solve2b(nums)
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                ans += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return ans
    def solve2a(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        cnt = [0] * (mx + n)
        for x in nums:
            cnt[x] += 1
        ans = 0
        left = []
        for x in range(mx + n):
            if cnt[x] >= 2:
                left.extend([x] * (cnt[x] - 1))
            elif left and cnt[x] == 0:
                ans += x - left.pop()
        return ans
    def solve2b(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        cnt = [0] * (mx + n)
        for x in nums:
            cnt[x] += 1
        ans = 0
        left = 0
        for x in range(mx + n):
            if cnt[x] >= 2:
                left += cnt[x] - 1
                ans -= x * (cnt[x] - 1)
            elif left > 0 and cnt[x] == 0:
                ans += x
                left -= 1
        return ans
# @lc code=end

sol = Solution()
print(sol.minIncrementForUnique([1,2,2])) # 1

#
# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,2,1,7]\n
# @lcpr case=end

#

