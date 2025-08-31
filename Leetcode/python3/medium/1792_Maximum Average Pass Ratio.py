#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
考慮增加 1 個學生後的貢獻：
  (a + 1)/(b + 1) - a/b
= (ba + b - ab - a)/b(b + 1)
= (b - a)/b(b + 1)
"""
# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        hp = [(-(b - a) / (b * (b + 1)), a, b) for a, b in classes]
        heapify(hp)
        for _ in range(extraStudents):
            a, b = hp[0][1] + 1, hp[0][2] + 1
            heapreplace(hp, (-(b - a) / (b * (b + 1)), a, b))
        return sum(a / b for _, a, b in hp) / n
# @lc code=end

sol = Solution()
print(sol.maxAverageRatio([[1,2],[3,5],[2,2]], 2))  # 0.78333