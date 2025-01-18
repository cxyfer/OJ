#
# @lc app=leetcode.cn id=8041 lang=python3
#
# [8041] 完全子集的最大元素和
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        枚舉core()為i的下標
        好像懂了又好像沒懂
    """
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            s = 0
            for j in range(1, isqrt(n // i) + 1):
                s += nums[i * j * j - 1]  # -1 是因为数组下标从 0 开始
            ans = max(ans, s)
        return ans

# @lc code=end

