#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
from en.Python3.mod.preImport import *
from collections import deque
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic stack
        # Similar to 42. Trapping Rain Water
        # 找左右比當前矮的柱子
        ans = 0
        # 左右加入高度為0的柱子
        heights.insert(0, 0)
        heights.append(0)

        stack = deque()
        stack.append(0)
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop() # idx 為當前的柱子
                if stack:
                    # i 為右邊比當前矮的柱子，stack[-1]為左邊比當前矮的柱子
                    h = heights[idx] 
                    w = i - stack[-1] - 1 # 高度為h的柱子可以向左右延伸的最大寬度
                    ans = max(ans, h * w)
            stack.append(i)
        return ans
# @lc code=end

