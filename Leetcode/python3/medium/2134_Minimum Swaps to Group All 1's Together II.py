#
# @lc app=leetcode id=2134 lang=python3
# @lcpr version=30204
#
# [2134] Minimum Swaps to Group All 1's Together II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        k = nums.count(1)
        ans = k
        cnt = sum(nums[:k])
        left = 0
        for right in range(k, n + k):
            cnt += nums[right % n]
            ans = min(ans, k - cnt)
            left += 1
        
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,0,1]\n
# @lcpr case=end

#

