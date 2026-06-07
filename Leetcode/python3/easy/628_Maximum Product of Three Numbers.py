#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def maximumProduct(self, nums: List[int]) -> int:
        pos = sorted([x for x in nums if x >= 0], reverse=True)
        neg = sorted([x for x in nums if x < 0])

        ans = float("-inf")
        if len(pos) >= 3:
            ans = max(ans, pos[0] * pos[1] * pos[2])
        if len(pos) >= 1 and len(neg) >= 2:
            ans = max(ans, pos[0] * neg[0] * neg[1])
        if len(pos) >= 2 and len(neg) >= 1:
            ans = max(ans, pos[-1] * pos[-2] * neg[-1])
        if len(neg) >= 3:
            ans = max(ans, neg[-3] * neg[-2] * neg[-1])
        return ans


class Solution1b:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])


class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        L = nlargest(3, nums)
        S = nsmallest(2, nums)
        return max(L[0] * L[1] * L[2], L[0] * S[0] * S[1])


# Solution = Solution1a
# Solution = Solution1b
Solution = Solution2
# @lc code=end

