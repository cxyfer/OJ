#
# @lc app=leetcode id=1590 lang=python3
# @lcpr version=30204
#
# [1590] Make Sum Divisible by P
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        r = sum(nums) % p
        if r == 0:
            return 0
        s = 0 # prefix sum
        pos = {0: -1}
        ans = n
        for i, x in enumerate(nums):
            s = (s + x) % p
            if (s - r) % p in pos:
                ans = min(ans, i - pos[(s - r) % p])
            pos[s] = i
        return ans if ans < n else -1
# @lc code=end



#
# @lcpr case=start
# [3,1,4,2]\n6\n
# @lcpr case=end

# @lcpr case=start
# [6,3,5,2]\n9\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

