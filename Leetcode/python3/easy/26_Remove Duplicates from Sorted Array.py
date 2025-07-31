#
# @lc app=leetcode id=26 lang=python3
# @lcpr version=30204
#
# [26] Remove Duplicates from Sorted Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = k = 0
        while (i < n):
            j = i
            while (i < n and nums[j] == nums[i]):
                i += 1
            nums[k] = nums[j]
            k += 1
        return k
    
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

# Solution = Solution1
Solution = Solution2
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

