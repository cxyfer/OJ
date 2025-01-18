#
# @lc app=leetcode id=560 lang=python3
# @lcpr version=30203
#
# [560] Subarray Sum Equals K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Prefix Sum + Hash Table
        Same as 930. Binary Subarrays With Sum
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            s += x
            ans += cnt[s - k]
            cnt[s] += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

