#
# @lc app=leetcode id=3634 lang=python3
#
# [3634] Minimum Removals to Balance Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = n
        for i, x in enumerate(nums):  # 枚舉最小值
            j = bisect_right(nums, x * k)
            ans = min(ans, n - (j - i))
        return ans
    
class Solution2:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = n
        j = 0
        for i, x in enumerate(nums):
            while j < n and nums[j] <= x * k:
                j += 1
            ans = min(ans, n - (j - i))
        return ans
    
# Solution = Solution1
Solution = Solution2
# @lc code=end 

sol = Solution()
print(sol.minRemoval([2,1,5], 2))  # 1
print(sol.minRemoval([1,6,2,9], 3))  # 2
print(sol.minRemoval([4,6], 2))  # 0