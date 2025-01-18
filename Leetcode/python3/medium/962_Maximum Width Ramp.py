#
# @lc app=leetcode id=962 lang=python3
# @lcpr version=30204
#
# [962] Maximum Width Ramp
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Monotonic Stack
    """
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        for i, x in enumerate(nums):
            if not st or nums[st[-1]] > x:
                st.append(i)
        ans = 0
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                ans = max(ans, i - st[-1])
                st.pop()
        return ans
# @lc code=end



#
# @lcpr case=start
# [6,0,8,2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [9,8,1,0,1,9,4,0,4,1]\n
# @lcpr case=end

#

