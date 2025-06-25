#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        def check(mx):
            cnt = 0
            j = m - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mx:
                    j -= 1
                cnt += j + 1
            return cnt >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

