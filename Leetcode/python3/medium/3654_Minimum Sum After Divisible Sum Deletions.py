#
# @lc app=leetcode id=3654 lang=python3
#
# [3654] Minimum Sum After Divisible Sum Deletions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        mp = [0] + [-1] * (k - 1)
        f = [0] * (n + 1)
        for i, x in enumerate(nums, start=1):
            s = (s + x) % k
            f[i] = min(f[i - 1] + x, f[mp[s]] if mp[s] != -1 else float('inf'))
            mp[s] = i
        return f[n]

class Solution1b:
    def minArraySum(self, nums: List[int], k: int) -> int:
        mp = [0] + [float('inf')] * (k - 1)
        s = f = 0
        for x in nums:
            s = (s + x) % k
            f = min(f + x, mp[s])
            mp[s] = f
        return f

# Solution = Solution1a   
Solution = Solution1b
# @lc code=end

