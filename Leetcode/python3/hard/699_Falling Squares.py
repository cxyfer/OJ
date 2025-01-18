#
# @lc app=leetcode id=699 lang=python3
# @lcpr version=30204
#
# [699] Falling Squares
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 暴力枚舉 O(n^2)
    2. 有序集合 O(n log n)
    3. 線段樹 O(n log n)
"""
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        h = [0] * n # 第 i 個方塊的高度
        for i, (left, length) in enumerate(positions):
            right = left + length - 1 # 當前方塊的右端點
            h[i] = length # 當前方塊的高度
            for j in range(i): # 檢查當前方塊是否放在其他方塊上面
                left2, right2 = positions[j][0], positions[j][0] + positions[j][1] - 1
                if right >= left2 and left <= right2:
                    # 如果方塊的左端點在其他方塊的右端點之前，且右端點在其他方塊的左端點之後，則更新方塊的高度
                    h[i] = max(h[i], h[j] + length)
        # 將 h 更新為放置第 i 個方塊後的最高高度，注意最高高度可能比第 i 個方塊的高度高
        for i in range(1, n):
            h[i] = max(h[i], h[i - 1])
        return h
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[6,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[100,100],[200,100]]\n
# @lcpr case=end

#

