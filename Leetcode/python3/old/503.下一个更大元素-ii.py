#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
from en.Python3.mod.preImport import *
from collections import deque
# @lc code=start
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
# @lc code=end

