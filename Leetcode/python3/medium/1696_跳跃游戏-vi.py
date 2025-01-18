#
# @lc app=leetcode.cn id=1696 lang=python3
#
# [1696] 跳跃游戏 VI
#
from preImport import *
# @lc code=start
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hp = [] # max heap
        ans = nums[0]
        heappush(hp, (-nums[0], 0)) # (value, index)
        for i in range(1, n):
            while hp and i - hp[0][1] > k: # index distance is too large
                heappop(hp)
            ans = -hp[0][0] + nums[i]
            heappush(hp, (-ans, i))
        return ans
# @lc code=end

sol = Solution()
print(sol.maxResult([1,-1,-2,4,-7,3],2)) # 7
print(sol.maxResult([10,-5,-2,4,0,3],3)) # 17
print(sol.maxResult([1,-5,-20,4,-1,3,-6,-3],2)) # 0
