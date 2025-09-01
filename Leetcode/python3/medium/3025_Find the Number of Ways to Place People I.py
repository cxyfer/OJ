#
# @lc app=leetcode id=3025 lang=python3
#
# [3025] Find the Number of Ways to Place People I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
目標是對於每個點 pi ，找到在pi右下方的點 pj ，且在pi和pj之間沒有其他點。

Hint: 如果我們固定左上角的點 (x, y)，那麼能夠與其構成答案的點有哪些？這些點會呈現怎樣的性質呢？
做圖後不難觀察到，這些點會呈現一個階梯狀，且越往下，y座標越小。

在右下方的點中，每一個 x 座標對應的點中，y座標最小的點才「有機會」構成答案。
為甚麼是「有機會」呢？因為這個 y 座標最小的點，可能會被左上方能構成答案的其他點影響，導致無法構成答案。

自此思路明確，我們先對 x 進行排序，使得當 j > i 時，pj 不是在 pi 的下方就是在 pi 的右方。
再來由於 y 座標最小的點才「有機會」構成答案，因此對 y 軸由小到大排序。
又考慮到左上方其他點可能會影響到右下方最小的點，因此紀錄能構成答案的點鐘最小的 y 座標。
"""
# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        # 枚舉 pi，並確保 pj 不是在 pi 的下方就是在 pi 的右方
        points.sort(key = lambda p: (-p[0], p[1]))
        for i, (_, y1) in enumerate(points):
            min_y = float("inf")  # 紀錄能構成答案的點鐘最小的 y 座標
            for j in range(i + 1, n):
                _, y2 = points[j]
                if y2 < y1:
                    continue
                if min_y > y2:  # 不會被左上方能構成答案的其他點影響
                    min_y = y2
                    ans += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.numberOfPairs([[1,1],[2,2],[3,3]]))  # 0
print(sol.numberOfPairs([[6,2],[4,4],[2,6]]))  # 2
print(sol.numberOfPairs([[3,1],[1,3],[1,1]]))  # 2