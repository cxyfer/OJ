#
# @lc app=leetcode id=3761 lang=python3
#
# [3761] Minimum Absolute Distance Between Mirror Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            # return int(str(x)[::-1])
            rev = 0
            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10
            return rev

        ans = float('inf')
        last = dict()
        for i, x in enumerate(nums):
            if x in last:
                ans = min(ans, i - last[x])
            rev = reverse(x)
            last[rev] = i
        return ans if ans < float('inf') else -1
# @lc code=end

sol = Solution()
print(sol.minMirrorPairDistance([120,21]))  # 1