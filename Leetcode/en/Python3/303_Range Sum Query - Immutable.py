# @algorithm @lc id=303 lang=python3 
# @title range-sum-query-immutable

from en.Python3.mod.preImport import *

class NumArray:

    def __init__(self, nums: List[int]):
        s = [0] * (len(nums)+1)
        for i, x in enumerate(nums):
            s[i+1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right+1] - self.s[left]