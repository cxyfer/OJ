#
# @lc app=leetcode.cn id=100031 lang=python3
#
# [100031] 计算 K 置位下标对应元素的和
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            if bin(idx).count('1') == k:
                ans += num
        return ans
# @lc code=end

sol = Solution()
print(sol.sumIndicesWithKSetBits([5,10,1,5,2],1))
print(sol.sumIndicesWithKSetBits([4,3,2,1],2))

