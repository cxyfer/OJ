#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
from en.Python3.mod.preImport import *
from collections import deque
# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Monotonic stack
        # Extension of 84. Largest Rectangle in Histogram
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        ans = 0
        for row in matrix:
            for i, c in enumerate(row):
                heights[i] = heights[i] + 1 if c == '1' else 0
            # 逐行算一次最大矩形面積，傳入的heights會被改變，所以要傳入副本
            ans = max(ans, self.largestRectangleArea(heights[:]))
        return ans

    # Same as 84. Largest Rectangle in Histogram
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
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

if __name__ == '__main__':
    sol = Solution()
    heights = [["1","0"],["1","0"]]
    print(sol.maximalRectangle(heights))

