#
# @lc app=leetcode id=3468 lang=python3
#
# [3468] Find the Number of Copy Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        lo, hi = -float('inf'), float('inf')
        for x, (l, r) in zip(original, bounds):
            d = x - original[0]
            hi = min(hi, r - d)
            lo = max(lo, l - d)
        return max(0, hi - lo + 1)
# @lc code=end

sol = Solution()
print(sol.countArrays([1,2,3,4], [[1,2],[2,3],[3,4],[4,5]]))  # 2
print(sol.countArrays([1,2,3,4], [[1,10],[2,9],[3,8],[4,7]]))  # 4
print(sol.countArrays([1,2,1,2], [[1,1],[2,3],[3,3],[2,3]]))  # 0
