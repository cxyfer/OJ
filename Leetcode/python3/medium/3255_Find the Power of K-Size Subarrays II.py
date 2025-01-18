#
# @lc app=leetcode id=3255 lang=python3
# @lcpr version=30204
#
# [3255] Find the Power of K-Size Subarrays II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 1
        ans[0] = nums[0] if k == 1 else -1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans[i - k + 1] = nums[i]
        return ans
    
class Solution2:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 0
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans[i - k + 1] = x
        return ans

class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,3,2,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,2,3,2]\n2\n
# @lcpr case=end

#

