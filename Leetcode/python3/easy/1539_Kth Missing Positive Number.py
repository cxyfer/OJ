#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def check(m):
            return arr[m] - (m + 1) >= k

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # return arr[right] + k - (arr[right] - (right + 1))
        return k + right + 1
# @lc code=end

sol = Solution()
print(sol.findKthPositive([2, 3, 4, 7, 11], 5))  # 9
print(sol.findKthPositive([1, 2, 3, 4], 2))  # 6
print(sol.findKthPositive([2], 1))  # 1
