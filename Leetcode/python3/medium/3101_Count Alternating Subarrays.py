#
# @lc app=leetcode id=3101 lang=python3
# @lcpr version=30204
#
# [3101] Count Alternating Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        dp = [1] * n
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            ans += dp[i]
        return ans
    
class Solution2:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = f = 1
        for x, y in pairwise(nums):
            if x != y:
                f += 1
            else:
                f = 1
            ans += f
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,0]\n
# @lcpr case=end

#

