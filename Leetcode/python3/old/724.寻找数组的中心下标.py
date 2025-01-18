#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        1. 前綴和
    """
    def pivotIndex(self, nums: List[int]) -> int:
        lprefix = [0]
        rprefix = [0]
        for num in nums:
            lprefix.append(lprefix[-1] + num)
        for num in nums[::-1]:
            rprefix.append(rprefix[-1] + num)
        rprefix = rprefix[::-1]
        for i in range(len(nums)):
            if lprefix[i] == rprefix[i+1]:
                return i
        return -1
    """
        2. 前綴和優化
    """
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        cur = 0
        for i in range(n):
            if cur * 2 + nums[i] == s: # if cur == s - cur - nums[i]
                return i
            cur += nums[i]
        return -1
    
# @lc code=end

