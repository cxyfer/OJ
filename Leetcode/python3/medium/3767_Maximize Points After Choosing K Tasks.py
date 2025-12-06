#
# @lc app=leetcode id=3767 lang=python3
#
# [3767] Maximize Points After Choosing K Tasks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        arr = [x - y for x, y in zip(technique1, technique2)]
        arr.sort(reverse=True)
        ans = sum(technique2)
        for i, d in enumerate(arr):  # 反悔貪心
            if i < k or d > 0:
                ans += d
        return ans
# @lc code=end

