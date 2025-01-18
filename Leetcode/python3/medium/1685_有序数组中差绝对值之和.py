#
# @lc app=leetcode.cn id=1685 lang=python3
#
# [1685] 有序数组中差绝对值之和
#
from preImport import *
# @lc code=start
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # 前綴和
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i-1]
        # 後綴和
        suf = [0] * n
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] + nums[i+1]
        # 計算答案
        for i in range(n):
            p = nums[i] * i - pre[i]
            s = suf[i] - nums[i] * (n-i-1)
            ans[i] = p + s
        return ans
# @lc code=end
sol = Solution()
print(sol.getSumAbsoluteDifferences([2,3,5])) # [4,3,5]
print(sol.getSumAbsoluteDifferences([1,4,6,8,10])) # [24,15,13,15,21]
