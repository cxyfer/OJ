#
# @lc app=leetcode id=3027 lang=python3
#
# [3027] Find the Number of Ways to Place People II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
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

