#
# @lc app=leetcode id=974 lang=python3
# @lcpr version=30203
#
# [974] Subarray Sums Divisible by K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0 # prefix sum
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            s += x
            ans += cnt[s % k]
            cnt[s % k] += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [4,5,0,-2,-3,1]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5]\n9\n
# @lcpr case=end

#

