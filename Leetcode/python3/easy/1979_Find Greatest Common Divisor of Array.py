#
# @lc app=leetcode id=1979 lang=python3
# @lcpr version=30201
#
# [1979] Find Greatest Common Divisor of Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = mn = nums[0]
        for x in nums:
            if x > mx: mx = x
            elif x < mn: mn = x
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
            # while b:
            #     a, b = b, a % b
            # return a
        return gcd(mx, mn)
# @lc code=end



#
# @lcpr case=start
# [2,5,6,9,10]\n
# @lcpr case=end

# @lcpr case=start
# [7,5,6,8,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n
# @lcpr case=end

#

