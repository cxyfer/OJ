# @algorithm @lc id=503 lang=python3 
# @title next-greater-element-ii


from en.Python3.mod.preImport import *
from collections import deque
# @test([1,2,1])=[2,-1,2]
# @test([1,2,3,4,3])=[2,3,4,-1,4]
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Monotonic stack
        # Similar to 739. Daily Temperatures
        # Using mod to simulate the circular array
        n = len(nums)
        ans = [-1] * n
        stack = deque()
        stack.append(0)
        for i in range(1, n * 2):
            idx = i % n
            while stack and nums[idx] > nums[stack[-1]]:
                ans[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        return ans