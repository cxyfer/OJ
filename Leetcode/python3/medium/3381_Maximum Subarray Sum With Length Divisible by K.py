#
# @lc app=leetcode id=3381 lang=python3
# @lcpr version=30204
#
# [3381] Maximum Subarray Sum With Length Divisible by K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
前綴和 + 同餘

若 i % k == j % k，則 s[i] - s[j] 必為 k 的倍數，因此我們可以枚舉 i 、考慮 j 。
為了使 s[i] - s[j] 最大，由於 s[i] 固定，我們需要使 s[j] 最小。
因此我們可以維護一個長度為 k 的陣列，用來儲存 s[j % k] 的最小值。
"""
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        mp = [float('inf')] * k
        ans = -float('inf')
        for i in range(n + 1):
            m = i % k
            ans = max(ans, s[i] - mp[m])
            mp[m] = min(mp[m], s[i])
        return ans 
# @lc code=end



#
# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [-1,-2,-3,-4,-5]\n4\n
# @lcpr case=end

# @lcpr case=start
# [-5,1,2,-3,4]\n2\n
# @lcpr case=end

#

