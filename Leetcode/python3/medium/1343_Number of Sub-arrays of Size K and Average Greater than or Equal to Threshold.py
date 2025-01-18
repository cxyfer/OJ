#
# @lc app=leetcode id=1343 lang=python3
# @lcpr version=30204
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = cur = 0
        target = k * threshold
        for idx, x in enumerate(arr):
            cur += x
            if idx < k - 1:
                continue
            ans += cur >= target
            cur -= arr[idx - k + 1]
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,2,2,2,5,5,5,8]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [11,13,17,23,29,31,7,5,2,3]\n3\n5\n
# @lcpr case=end

#

