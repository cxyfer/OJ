# @algorithm @lc id=167 lang=python3 
# @title two-sum-ii-input-array-is-sorted


from en.Python3.mod.preImport import *
# @test([2,7,11,15],9)=[1,2]
# @test([2,3,4],6)=[1,3]
# @test([-1,0],-1)=[1,2]
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