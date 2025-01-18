#
# @lc app=leetcode id=2644 lang=python3
# @lcpr version=30202
#
# [2644] Find the Maximum Divisibility Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mx, ans = -1, 0
        for d in divisors:
            cur = 0 # count of numbers divisible by d
            for x in nums:
                if x % d == 0:
                    cur += 1
            if cur > mx or (cur == mx and d < ans): # update answer
                mx, ans = cur, d
        return ans
# @lc code=end



#
# @lcpr case=start
# [4,7,9,3,9]\n[5,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [20,14,21,10]\n[5,7,5]\n
# @lcpr case=end

# @lcpr case=start
# [12]\n[10,16]\n
# @lcpr case=end

#

