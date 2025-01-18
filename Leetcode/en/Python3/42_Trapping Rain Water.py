# @algorithm @lc id=42 lang=python3 
# @title trapping-rain-water


from en.Python3.mod.preImport import *
from collections import deque
# @test([0,1,0,2,1,0,1,3,2,1,2,1])=6
# @test([4,2,0,3,2,5])=9
class Solution:
    def trap(self, height: List[int]) -> int:
        # return self.solve1(height)
        return self.solve2(height)
        # return self.solve3(height)
    """
        1a. 縱向求解：動態規劃
        維護 前綴最大值 和 後綴最大值
        Time: O(n)
        Space: O(n)
    """
    def solve1(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [height[0]] + [0] * (n-1) # 前綴最大值
        suf_max = [0] * (n-1) + [height[-1]] # 後綴最大值
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        ans = 0
        for i in range(n):
            ans += min(pre_max[i], suf_max[i]) - height[i] # 木桶原理，取決於前綴和後綴的最小值
        return ans
    """
        1b. 縱向求解：雙指標
        一邊更新答案一邊 維護 前綴最大值 和 後綴最大值
        若左邊的高度比右邊小，則考慮左邊的水量，其取決於左邊的最大值，因為後綴最大值只會>=右邊的高度，反之亦然

        Time: O(n)
        Space: O(1)
    """
    def solve2(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        pre_max, suf_max = 0, 0 # 維護 前綴最大值 和 後綴最大值
        ans = 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if height[left] < height[right]: # 若左邊的高度比右邊小，則考慮左邊的水量
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
    """
        2. 橫向求解：單調棧
        Stack 中存放的是下標，對應的元素是由下到上遞減的
        Time: O(n)
    """
    def solve3(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        st = deque()
        for i in range(n):
            while st and height[i] > height[st[-1]]:
                idx = st.pop() # 當前柱子
                if st:
                    left = height[st[-1]] # 左邊比當前高的柱子
                    right = height[i] # 右邊比當前高的柱子
                    h = min(left, right) - height[idx]
                    w = i - st[-1] - 1
                    ans += h * w
            st.append(i)
        return ans