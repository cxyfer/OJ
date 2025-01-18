#
# @lc app=leetcode.cn id=1846 lang=python3
#
# [1846] 减小和重新排列数组后的最大元素
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy
        滿足題意的array一定是單調遞增的
    """
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        arr[0] = 1
        for i in range(1, n):
            # if arr[i] - arr[i-1] > 1:
            #     arr[i] = arr[i-1] + 1
            arr[i] = min(arr[i], arr[i-1]+1)
        return arr[-1]
# @lc code=end

