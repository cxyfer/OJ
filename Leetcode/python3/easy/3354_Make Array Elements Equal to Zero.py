#
# @lc app=leetcode id=3354 lang=python3
#
# [3354] Make Array Elements Equal to Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot = sum(nums)
        ans = s = 0
        for x in nums:
            s += x
            if x == 0:
                d = abs(tot - 2 * s)
                if d == 0:
                    ans += 2
                elif d == 1:
                    ans += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.countValidSelections([1,0,2,0,3]))  # 2