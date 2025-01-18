#
# @lc app=leetcode id=1608 lang=python3
# @lcpr version=30202
#
# [1608] Special Array With X Elements Greater Than or Equal X
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Sort
        Similar to 274. H-Index
    """
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        for i, x in enumerate(nums, 1):
            # 比 i 大的數至少有 i 個，且比 i 大的數不超過 i 個，即比 i 大的數恰好有 i 個
            if x >= i and (i == n or nums[i] < i): 
                return i
        return -1
# @lc code=end

sol = Solution()
print(sol.specialArray([3,5])) # 2
print(sol.specialArray([0,0])) # -1

#
# @lcpr case=start
# [3,5]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,4,3,0,4]\n
# @lcpr case=end

#

