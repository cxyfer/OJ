#
# @lc app=leetcode id=2342 lang=python3
# @lcpr version=30204
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(x):
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res
        ans = -1
        mp = defaultdict(lambda : float("-inf"))
        for x in nums:
            d = digit_sum(x)
            ans = max(ans, x + mp[d])
            mp[d] = max(mp[d], x)
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumSum([18,43,36,13,7]))


#
# @lcpr case=start
# [18,43,36,13,7]\n
# @lcpr case=end

# @lcpr case=start
# [10,12,19,14]\n
# @lcpr case=end

#

