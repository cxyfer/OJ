#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from preImport import *
# @lc code=start
class Solution:
    """
        > 基础算法精讲 01
        反向(相向)雙指標
        利用 numbers 已經由小到大非遞減排序的特性，可以使用反向雙指標
        TC: O(n)
        SC: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right: # 區間內至少要有兩個數字
            s = numbers[left] + numbers[right]
            if s == target: # 找到答案
                return [left+1,right+1]
            elif s > target: # 去除最大的數
                right -= 1
            else: # 去除最小的數
                left += 1
        return [-1,-1]
# @lc code=end

