# @algorithm @lc id=724 lang=python3 
# @title find-pivot-index


from en.Python3.mod.preImport import *
# @test([1,7,3,6,5,6])=3
# @test([1,2,3])=-1
# @test([2,1,-1])=0
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