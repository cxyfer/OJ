#
# @lc app=leetcode.cn id=2560 lang=python3
#
# [2560] 打家劫舍 IV
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        最大化最小值/最小化最大值 => Binary Search
        1. Binary Search + Dynamic Programming
        2. Binary Search + Greedy
    """
    def minCapability(self, nums: List[int], k: int) -> int:
        def dp(mx: int) -> int: # dp(mx) 表示能力不超過 mx 時的最大搶劫屋數
            f0 = f1 = 0
            for x in nums:
                if x > mx: # 超出能力，一定不能偷
                    f0 = f1
                else: # 沒超出能力，可以偷也可以不偷
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1
        def greedy(mx: int) -> int: # greedy(mx) 表示能力不超過 mx 時的最大搶劫屋數
            cnt = i = 0
            while i < len(nums):
                if nums[i] > mx: # 超出能力，一定不能偷
                    i += 1
                else: # 沒超出能力，但能偷就偷一定有最大搶劫屋數
                    cnt += 1
                    i += 2 
            return cnt
        return bisect_left(range(max(nums)), k, key=dp)
# @lc code=end

