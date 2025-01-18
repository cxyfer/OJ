#
# @lc app=leetcode.cn id=2997 lang=python3
#
# [2997] 使数组异或和等于 K 的最少操作次数
#
from preImport import *
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for num in nums:
            x ^= num
        ans = 0
        while x or k:
            if x & 1 != k & 1:
                ans += 1
            x >>= 1
            k >>= 1
        return ans
# @lc code=end
sol = Solution()
print(sol.minOperations([2,1,3,4],1)) # 2
print(sol.minOperations([2,0,2,0],0)) # 0
