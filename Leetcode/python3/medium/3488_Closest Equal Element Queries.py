#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        dist = [float("inf")] * n
        for k, lst in pos.items():
            m = len(lst)
            if m <= 1:
                continue
            for i, idx in enumerate(lst):
                dist[idx] = min(abs(lst[(i - 1) % m] - idx), n - abs(lst[(i - 1) % m] - idx),
                                abs(idx - lst[(i + 1) % m]), n - abs(idx - lst[(i + 1) % m]))
        return [dist[q] if dist[q] != float("inf") else -1 for q in queries]
# @lc code=end

