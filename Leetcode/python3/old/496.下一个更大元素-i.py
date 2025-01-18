#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
from en.Python3.mod.preImport import *
from collections import deque
# @lc code=start
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
# @lc code=end

