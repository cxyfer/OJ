#
# @lc app=leetcode id=152 lang=python3
# @lcpr version=30204
#
# [152] Maximum Product Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n)]  # (max, min)
        f[0] = [nums[0], nums[0]]
        for i in range(1, n):
            f[i][0] = max(nums[i], f[i - 1][0] * nums[i], f[i - 1][1] * nums[i])
            f[i][1] = min(nums[i], f[i - 1][0] * nums[i], f[i - 1][1] * nums[i])
        return max(f[i][0] for i in range(n))
    
class Solution1b:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max_val = min_val = nums[0]
        for i in range(1, n):
            new_max_val = max(nums[i], max_val * nums[i], min_val * nums[i])
            new_min_val = min(nums[i], max_val * nums[i], min_val * nums[i])
            max_val, min_val = new_max_val, new_min_val
            ans = max(ans, max_val)
        return ans

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max_val = min_val = nums[0]
        for i in range(1, n):
            if nums[i] < 0: max_val, min_val = min_val, max_val # 遇到負數，最大值和最小值互換
            max_val = max(nums[i], max_val * nums[i]) 
            min_val = min(nums[i], min_val * nums[i])
            ans = max(ans, max_val)
        return ans

class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#

