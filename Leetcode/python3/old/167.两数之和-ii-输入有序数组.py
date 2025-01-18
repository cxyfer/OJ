#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 反向雙指標
        # 由於 numbers 已經排序，所以可以使用反向雙指針
        n = len(numbers) # numbers 已經非遞減由小到大排序
        left, right = 0, n-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1 # 去除最大的數
            else:
                left += 1 # 去除最小的數
# @lc code=end

