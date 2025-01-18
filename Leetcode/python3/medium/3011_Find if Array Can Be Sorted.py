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
            i += 1
            while i < n and nums[i].bit_count() == cnt:
                i += 1
            nums[st:i] = sorted(nums[st:i])
        return all(x <= y for x, y in pairwise(nums))
    
class Solution2:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        pre_mx = -1
        while i < n:
            mx = nums[i]
            cnt = nums[i].bit_count()
            while i < n and nums[i].bit_count() == cnt:
                if nums[i] < pre_mx:
                    return False
                mx = max(mx, nums[i])
                i += 1
            pre_mx = mx
        return True
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



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

