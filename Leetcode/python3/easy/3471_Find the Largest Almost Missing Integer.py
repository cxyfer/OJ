#
# @lc app=leetcode id=3471 lang=python3
#
# [3471] Find the Largest Almost Missing Integer
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k:
            return max(nums)
        ans = -1
        cnt = Counter(nums)
        for i in [0, n - 1] if k > 1 else range(n):
            if cnt[nums[i]] == 1:
                ans = max(ans, nums[i])
        return ans
# @lc code=end

sol = Solution()
print(sol.largestInteger([3,1,7,10,0], 1))  # 10

