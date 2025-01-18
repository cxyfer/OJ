#
# @lc app=leetcode id=3194 lang=python3
# @lcpr version=30204
#
# [3194] Minimum Average of Smallest and Largest Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        ans = float("inf")
        left, right = 0, n - 1
        while left < right:
            ans = min(ans, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return ans
    
class Solution2:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        return min(nums[i] + nums[n - 1 - i] for i in range(n // 2)) / 2
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [7,8,3,4,15,13,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,9,8,3,10,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,7,8,9]\n
# @lcpr case=end

#

