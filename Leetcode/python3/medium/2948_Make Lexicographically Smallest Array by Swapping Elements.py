#
# @lc app=leetcode id=2948 lang=python3
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    排序 + 分組循環
"""
# @lc code=start
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        ans = [0] * n

        A = [(i, x) for i, x in enumerate(nums)]
        A.sort(key=lambda x: x[1])

        i = 0
        while i < n:
            idxs, vals = [A[i][0]], [A[i][1]]
            while i + 1 < n and A[i + 1][1] - A[i][1] <= limit:
                idxs.append(A[i + 1][0])
                vals.append(A[i + 1][1])
                i += 1
            idxs.sort()
            for idx, val in zip(idxs, vals):
                ans[idx] = val
            i += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.lexicographicallySmallestArray([1, 5, 3, 9, 8], 2))  # [1,3,5,8,9]