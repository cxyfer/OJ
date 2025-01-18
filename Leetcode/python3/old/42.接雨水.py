#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from en.Python3.mod.preImport import *
from collections import deque
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # Monotonic stack 
        # Similar to 739. Daily Temperatures

        # 1. 橫向求解
        # n = len(height)
        # ans = 0
        # stack = deque()
        # stack.append(0)
        # for i in range(1, n):
        #     if height[i] <= height[stack[-1]]:
        #         stack.append(i)
        #     else:
        #         while (stack and height[i] > height[stack[-1]]):
        #             idx = stack.pop()
        #             if stack:
        #                 left = height[stack[-1]] # 左邊比當前高的柱子
        #                 right = height[i] # 右邊比當前高的柱子
        #                 h = min(left, right) - height[idx] # 長方形高度
        #                 w = i - stack[-1] - 1 # 長方形寬度
        #                 ans += h * w
        #         stack.append(i)
        # return ans

        # 2. 縱向求解
        # Time: O(n)
        # Space: O(n)
        n = len(height)
        # Maintain 前綴最大值 and 後綴最大值
        pre_max = [height[0]] + [0] * (n-1)
        suf_max = [0] * (n-1) + [height[-1]]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        ans = 0
        for i in range(n):
            ans += min(pre_max[i], suf_max[i]) - height[i]
        return ans
# @lc code=end

