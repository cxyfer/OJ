#
# @lc app=leetcode id=3371 lang=python3
# @lcpr version=30204
#
# [3371] Identify the Largest Outlier in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        s = sum(nums)
        ans = -float('inf')
        for x in nums: # 枚舉 outlier
            if (s - x) & 1: continue
            cur = (s - x) // 2
            if cur != x and cnt[cur] > 0 or cur == x and cnt[cur] > 1:
                ans = max(ans, x)
        return ans
# @lc code=end
sol = Solution()
nums = [874,159,-838,-375,658]
print(sol.getLargestOutlier(nums)) # -838
nums = [958,777,-746,566,989]
print(sol.getLargestOutlier(nums)) # 566

#
# @lcpr case=start
# [2,3,5,10]\n
# @lcpr case=end

# @lcpr case=start
# [-2,-1,-3,-6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1,5,5]\n
# @lcpr case=end

#

