# @algorithm @lc id=84 lang=python3 
# @title largest-rectangle-in-histogram


from en.Python3.mod.preImport import *
from collections import deque
# @test([2,1,5,6,2,3])=10
# @test([2,4])=4
class Solution:
    """
        Monotonic stack
        Similar to 42. Trapping Rain Water
        找左右比當前矮的柱子
        在Stack存放的是index，但對應的element是由下到上遞增的
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights = [0] + heights + [0] # 左右加入高度為0的柱子
        n = len(heights)
        st = [] # 
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                idx = st.pop() # idx 為當前的柱子
                if st:
                    # i 為右邊比當前矮的柱子，stack[-1]為左邊比當前矮的柱子
                    h = heights[idx]
                    w = i - st[-1] - 1  # 高度為h的柱子可以向左右延伸的最大寬度
                    ans = max(ans, h * w)
            st.append(i)
        return ans