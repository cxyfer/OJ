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

        dist = [-1] * n
        for _, lst in pos.items():
            m = len(lst)
            if m <= 1:
                continue
            for i, idx in enumerate(lst):
                d1 = abs(lst[(i - 1) % m] - idx)
                d2 = abs(idx - lst[(i + 1) % m])
                dist[idx] = min(d1, d2, n - d1, n - d2)
        return [dist[q] for q in queries]
# @lc code=end

