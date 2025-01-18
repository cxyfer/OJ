#
# @lc app=leetcode id=3366 lang=python3
# @lcpr version=30204
#
# [3366] Minimum Array Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        @cache
        def f(i: int, cnt1: int, cnt2: int) -> int:
            if i == n:
                return 0

            x = nums[i] 

            res = x + f(i + 1, cnt1, cnt2) # 不操作
            if cnt1 < op1:
                res = min(res, math.ceil(x / 2) + f(i + 1, cnt1 + 1, cnt2)) # 操作1

            if cnt2 < op2 and x >= k:
                res = min(res, x - k + f(i + 1, cnt1, cnt2 + 1)) # 操作2

            if cnt1 < op1 and cnt2 < op2:
                x1 = math.ceil(x / 2)
                if x1 >= k:
                    res = min(res, x1 - k + f(i + 1, cnt1 + 1, cnt2 + 1)) # 先操作1後操作2
                if x >= k:
                    x2 = x - k
                    res = min(res, math.ceil(x2 / 2) + f(i + 1, cnt1 + 1, cnt2 + 1)) # 先操作2後操作1
            return res
        return f(0, 0, 0)
# @lc code=end

sol = Solution()
print(sol.minArraySum([2,8,3,19,3], 3, 1, 1)) # 23
print(sol.minArraySum([823,623,761,979], 426, 3, 4)) # 628

#
# @lcpr case=start
# [2,8,3,19,3]\n3\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n3\n2\n1\n
# @lcpr case=end

#

