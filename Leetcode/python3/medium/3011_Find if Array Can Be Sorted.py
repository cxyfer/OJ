#
# @lc app=leetcode id=3011 lang=python3
# @lcpr version=30204
#
# [3011] Find if Array Can Be Sorted
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            st = i
            cnt = nums[i].bit_count()
            while i < n and nums[i].bit_count() == cnt:
                i += 1
            nums[st:i] = sorted(nums[st:i])
        return all(x <= y for x, y in pairwise(nums))
    
class Solution2:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        pre = float('-inf')  # 前一段的最大值
        while i < n:
            st = i
            cnt = nums[i].bit_count()
            while i < n and nums[i].bit_count() == cnt:
                if nums[i] < pre:
                    return False
                i += 1
            pre = max(nums[st:i])
        return True
    
# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.canSortArray([20,16]))

#
# @lcpr case=start
# [8,4,2,30,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,16,8,4,2]\n
# @lcpr case=end

#

