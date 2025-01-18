#
# @lc app=leetcode id=930 lang=python3
# @lcpr version=30203
#
# [930] Binary Subarrays With Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Prefix Sum + Hash Table
        Same as 560. Subarray Sum Equals K
    """
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        s = 0 # prefix sum
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            s += x
            ans += cnt[s - goal]
            cnt[s] += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,0,1,0,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n0\n
# @lcpr case=end

#

