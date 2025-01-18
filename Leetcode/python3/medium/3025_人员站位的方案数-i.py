#
# @lc app=leetcode.cn id=3025 lang=python3
#
# [3025] 人员站位的方案数 I
#
from preImport import *
# @lc code=start
class Solution:
    """
        核心：枚舉每個點 pi ，往右下方向找到符合條件的點 pj
        依照 x 升序，y 降序排序，確保在pi下方或是右方的點都在pi後面，如此可以不用考慮x座標
        枚舉 pi ，找到在pi下方或是右方的點 pj ，且中間沒有其他點
    """
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        points.sort(key=lambda p: (p[0], -p[1])) # sort by x, -y
        for i in range(n): # 枚舉 pi
            x, y = points[i]
            max_y = -float("inf") # 記錄在pi下方或是右方的點中的最大y座標，用來確保中間沒有其他點
            for j in range(i+1, n): # 枚舉在pi下方或是右方的點 pj
                x2, y2 = points[j]
                if y2 > y: # 在 pi 右上方，不需要考慮
                    continue
                if max_y < y2: # 在 pi 下方、右方、右下方，且中間沒有其他點
                    max_y = y2
                    ans += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.numberOfPairs([[1,1],[2,2],[3,3]])) # 0
print(sol.numberOfPairs([[6,2],[4,4],[2,6]])) # 2
print(sol.numberOfPairs([[3,1],[1,3],[1,1]])) # 2
print(sol.numberOfPairs([[0,1],[1,3],[6,1]])) # 2
print(sol.numberOfPairs([[0,5],[4,4],[1,6]])) # 2