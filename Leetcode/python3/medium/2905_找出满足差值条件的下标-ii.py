#
# @lc app=leetcode.cn id=2905 lang=python3
#
# [2905] 找出满足差值条件的下标 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        Similar to 121. Best Time to Buy and Sell Stock
    """
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    return [i,j]
        return [-1,-1]
# @lc code=end

