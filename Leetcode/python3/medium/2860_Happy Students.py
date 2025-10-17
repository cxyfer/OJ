#
# @lc app=leetcode id=2860 lang=python3
#
# [2860] Happy Students
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
腦筋急轉彎

若當前選了 k 人，則：
- nums[i] < k 的 i 一定要被選，否則會不開心
- nums[i] > k 的 i 一定不能被選，否則會不開心
因此此時選的必然是最小的 k 個人
"""
# @lc code=start
class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = int(nums[0] > 0)
        for k in range(1, n):
            if nums[k - 1] < k < nums[k]:
                ans += 1
        ans += int(nums[n - 1] < n)  # 但題目保證 nums[n - 1] < n 成立，可以直接 + 1
        return ans
# @lc code=end

sol = Solution()
print(sol.countWays([1,1]))  # 2
print(sol.countWays([6,0,3,3,6,7,2,7]))  # 3
