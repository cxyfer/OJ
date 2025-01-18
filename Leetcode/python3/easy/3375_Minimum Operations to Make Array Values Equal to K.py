#
# @lc app=leetcode id=3375 lang=python3
# @lcpr version=30204
#
# [3375] Minimum Operations to Make Array Values Equal to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter(nums)
        for x in cnt.keys():
            if x < k:
                return -1
            ans += x > k
        return ans
# @lc code=end



#
# @lcpr case=start
# [5,2,5,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [9,7,5,3]\n1\n
# @lcpr case=end

#

