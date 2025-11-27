#
# @lc app=leetcode id=3381 lang=python3
# @lcpr version=30204
#
# [3381] Maximum Subarray Sum With Length Divisible by K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
前綴和 + 同餘

若 i % k == j % k，則 s[i] - s[j] 必為 k 的倍數，因此我們可以枚舉 i 、考慮 j 。
為了使 s[i] - s[j] 最大，由於 s[i] 固定，我們需要使 s[j] 最小。
因此我們可以維護一個長度為 k 的陣列，用來儲存 s[j % k] 的最小值。
"""
# @lc code=start
max = lambda a, b: a if a > b else b
min = lambda a, b: a if a < b else b
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = float('-inf')
        mp = [0] + [float('inf')] * (k - 1)
        s = 0
        for i, x in enumerate(nums, start=1):
            s += x
            m = i % k
            ans = max(ans, s - mp[m])
            mp[m] = min(mp[m], s)
        return ans
# @lc code=end

sol = Solution()
print(sol.maxSubarraySum([1,2], 1)) # 3
print(sol.maxSubarraySum([-1,-2,-3,-4,-5], 4))  # -10
print(sol.maxSubarraySum([-5,1,2,-3,4], 2))  # 4

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

