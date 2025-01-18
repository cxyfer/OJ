# @algorithm @lc id=496 lang=python3 
# @title next-greater-element-i


from en.Python3.mod.preImport import *
from collections import deque
# @test([4,1,2],[1,3,4,2])=[-1,3,-1]
# @test([2,4],[1,2,3,4])=[3,-1]
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Monotonic stack
        ans = [-1] * len(nums1)
        stack = deque()
        stack.append(0)
        hashMap = {num:i for i, num in enumerate(nums1)}
        
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in hashMap:
                        index = hashMap.get(nums2[stack[-1]])
                        ans[index] = nums2[i]
                    stack.pop()
                stack.append(i)
        return ans