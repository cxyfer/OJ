#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        ans = p1 = p2 = 0
        while idx < n:
            if nums[idx] == 1:
                p2 += 1
            else:
                p1 = p2
                p2 = 0
            idx += 1
            ans = max(ans, p1+p2)
        return ans-1 if ans == n else ans
# @lc code=end
sol = Solution()
print(sol.longestSubarray([1,1,0,1]))
print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(sol.longestSubarray([1,1,1]))
