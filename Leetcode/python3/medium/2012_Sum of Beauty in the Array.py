#
# @lc app=leetcode.cn id=2012 lang=python3
# @lcpr version=30204
#
# [2012] 数组美丽值求和
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        sufMin = [-1] * n
        sufMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            sufMin[i] = min(sufMin[i + 1], nums[i])
        ans = 0
        preMax = nums[0]
        for i in range(1, n - 1):
            x = nums[i]
            if preMax < nums[i] < sufMin[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
            preMax = max(preMax, nums[i])
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#

